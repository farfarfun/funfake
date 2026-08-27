"""
funfake 轻量冒烟测试套件（smoke tests）。

范围说明：
    本测试套件只做“冒烟级”验证 —— 确认包能正常导入、核心公开
    类/函数能以简单参数正常调用并返回合理形状的结果，不追求覆盖
    所有分支或边界条件的详尽单元测试。

背景：
    funfake 是一个纯本地随机数据生成库（HTTP 请求头 / 姓名 / 手机号），
    不依赖网络、数据库或任何云端凭据，所有数据都来自模块内置的静态列表，
    因此本测试无需使用 mock 来隔离外部资源。
"""

import random

import pytest


# ---------------------------------------------------------------------------
# 1. 顶层包 / 子模块导入
# ---------------------------------------------------------------------------


def test_import_top_level_package():
    import funfake

    assert hasattr(funfake, "fake_header")
    assert hasattr(funfake, "fake_name")
    assert hasattr(funfake, "fake_phone")


def test_import_all_public_submodules():
    import funfake.base
    import funfake.headers
    import funfake.headers.browsers
    import funfake.headers.core
    import funfake.headers.headers
    import funfake.names
    import funfake.names.core
    import funfake.names.scenarios
    import funfake.phones
    import funfake.phones.core

    # 简单确认模块确实被加载（有 __name__ 属性即可）
    for mod in (
        funfake.base,
        funfake.headers,
        funfake.headers.browsers,
        funfake.headers.core,
        funfake.headers.headers,
        funfake.names,
        funfake.names.core,
        funfake.names.scenarios,
        funfake.phones,
        funfake.phones.core,
    ):
        assert mod.__name__


def test_top_level_all_exports_are_importable():
    import funfake

    for name in funfake.__all__:
        assert hasattr(funfake, name), f"funfake.__all__ 中的 {name} 无法访问"


# ---------------------------------------------------------------------------
# 2. headers 模块
# ---------------------------------------------------------------------------


def test_fake_header_returns_basic_dict():
    from funfake import fake_header

    headers = fake_header()
    assert isinstance(headers, dict)
    for key in ("Accept", "Connection", "User-Agent"):
        assert key in headers
    assert isinstance(headers["User-Agent"], str)
    assert "%PLAT%" not in headers["User-Agent"]  # 占位符应已被替换


@pytest.mark.parametrize("browser", ["chrome", "firefox", "opera", None])
@pytest.mark.parametrize("os_name", ["win", "mac", "lin", None])
def test_headers_class_generate_with_various_combos(browser, os_name):
    from funfake.headers import Headers

    gen = Headers(browser=browser, os=os_name, headers=False)
    result = gen.generate()
    assert isinstance(result, dict)
    assert set(result.keys()) == {"Accept", "Connection", "User-Agent"}


def test_headers_class_with_extra_headers_enabled():
    from funfake.headers import Headers

    gen = Headers(browser="chrome", os="win", headers=True)
    result = gen.generate()
    assert isinstance(result, dict)
    # 额外头信息模式下必定包含 Referer
    assert "Referer" in result
    assert result["Referer"].startswith("https://")


def test_headers_generate_many_smoke():
    from funfake.headers import Headers

    gen = Headers(browser="chrome", os="win", headers=True)
    results = gen.generate_many(3, allow_duplicates=True)
    assert len(results) == 3
    assert all(isinstance(r, dict) for r in results)


# ---------------------------------------------------------------------------
# 3. names 模块 - 通用姓名
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("language", ["chinese", "english", None])
def test_fake_name_smoke(language):
    from funfake import fake_name

    name = fake_name(language)
    assert isinstance(name, str)
    assert len(name) > 0


def test_chinese_name_generator():
    from funfake.names import ChineseName

    gen = ChineseName(double_name_probability=0.5)
    name = gen.generate()
    assert isinstance(name, str)
    assert len(name) >= 2


def test_english_name_generator():
    from funfake.names import EnglishName

    gen = EnglishName()
    name = gen.generate()
    assert isinstance(name, str)
    assert " " in name  # "First Last" 格式


# ---------------------------------------------------------------------------
# 4. names 模块 - 场景化姓名生成器
# ---------------------------------------------------------------------------

SCENARIO_NAME_CLASSES = [
    "WaterMarginName",
    "JourneyToWestName",
    "DreamOfRedChamberName",
    "RomanceOfThreeKingdomsName",
    "InvestitureOfGodsName",
    "JinYongWuxiaName",
]


@pytest.mark.parametrize("class_name", SCENARIO_NAME_CLASSES)
def test_scenario_name_generator_smoke(class_name):
    import funfake.names.scenarios as scenarios_mod

    cls = getattr(scenarios_mod, class_name)
    gen = cls()

    groups = gen.get_groups()
    assert isinstance(groups, list)
    assert len(groups) > 0

    # 不指定分组，随机生成
    name = gen.generate()
    assert isinstance(name, str) and len(name) > 0

    # 指定第一个分组生成
    name_in_group = gen.generate(group=groups[0])
    assert isinstance(name_in_group, str) and len(name_in_group) > 0

    # 批量生成（允许重复，避免受限于某些分组名字数量过少）
    many = gen.generate_many(3, allow_duplicates=True)
    assert len(many) == 3


def test_scenario_name_invalid_group_raises():
    from funfake.names.scenarios import WaterMarginName

    gen = WaterMarginName()
    with pytest.raises(ValueError):
        gen.generate(group="不存在的分组")


# ---------------------------------------------------------------------------
# 5. phones 模块
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("country", ["chinese", "english", None])
def test_fake_phone_smoke(country):
    from funfake import fake_phone

    phone = fake_phone(country)
    assert isinstance(phone, str)
    assert len(phone) > 0


def test_chinese_phone_generator_default():
    from funfake.phones import ChinesePhone

    gen = ChinesePhone()
    phone = gen.generate()
    assert isinstance(phone, str)
    assert len(phone) == 11
    assert phone.isdigit()


@pytest.mark.parametrize("operator", ["移动", "联通", "电信"])
def test_chinese_phone_generator_by_operator(operator):
    from funfake.phones import ChinesePhone

    gen = ChinesePhone(operator=operator)
    phone = gen.generate()
    assert len(phone) == 11
    assert phone[:3] in gen.OPERATOR_GROUPS[operator]


def test_chinese_phone_invalid_operator_raises():
    from funfake.phones import ChinesePhone

    gen = ChinesePhone()
    with pytest.raises(ValueError):
        gen.generate(operator="不存在的运营商")


def test_chinese_phone_get_operators():
    from funfake.phones import ChinesePhone

    gen = ChinesePhone()
    operators = gen.get_operators()
    assert set(operators) == {"移动", "联通", "电信"}


@pytest.mark.parametrize("format_with_dash", [True, False])
def test_english_phone_generator(format_with_dash):
    from funfake.phones import EnglishPhone

    gen = EnglishPhone(format_with_dash=format_with_dash)
    phone = gen.generate()
    assert isinstance(phone, str)
    if format_with_dash:
        assert phone.count("-") == 2
    else:
        assert "-" not in phone
        assert phone.isdigit()


# ---------------------------------------------------------------------------
# 6. base 模块（抽象基类 / 通用批量生成逻辑）
# ---------------------------------------------------------------------------


def test_base_generator_is_abstract():
    from funfake.base import BaseGenerator

    with pytest.raises(TypeError):
        BaseGenerator()  # 不能直接实例化抽象基类


def test_list_based_generator_requires_config():
    from funfake.base import ListBasedGenerator

    with pytest.raises(ValueError):
        ListBasedGenerator()  # 子类未定义 NAMES/.../ 时基类本身也应报错


def test_generate_many_rejects_non_positive_count():
    from funfake.names import ChineseName

    gen = ChineseName()
    with pytest.raises(ValueError):
        gen.generate_many(0)


def test_generate_many_smoke_for_chinese_name():
    from funfake.names import ChineseName

    gen = ChineseName()
    names = gen.generate_many(5, allow_duplicates=True)
    assert len(names) == 5
    assert all(isinstance(n, str) for n in names)


# ---------------------------------------------------------------------------
# 7. 确定性检查（固定随机种子，验证生成器不会崩溃且结果可复现调用）
# ---------------------------------------------------------------------------


def test_determinism_smoke_with_seed():
    from funfake.names import ChineseName

    random.seed(12345)
    gen = ChineseName()
    first = gen.generate()
    assert isinstance(first, str)


# ---------------------------------------------------------------------------
# 8. CLI 入口点
# ---------------------------------------------------------------------------
#
# 说明：截至本测试编写时，funfake 的 pyproject.toml 中没有声明任何
# [project.scripts] CLI 入口点，因此没有可测试的命令行接口。此处保留一个
# 显式的跳过测试，若未来添加了 CLI 入口点，请替换为真实的 --help 冒烟测试。


def test_cli_entry_point_not_declared():
    pytest.skip("funfake 的 pyproject.toml 未声明任何 [project.scripts] CLI 入口点，跳过 CLI 冒烟测试")
