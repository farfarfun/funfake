# CHANGELOG

本文件记录 funfake 的版本变更，按版本倒序排列。

## [未发布]

### 新增

- 新增根目录 `CHANGELOG.md`。
- 补充 `tests/test_smoke.py` 对公开 API 边界/非法参数场景的覆盖：`fake_name`/`fake_phone`
  非法参数、`Headers.empty()`、`headers.headers.make_header()`。
- `[dependency-groups].dev` 补充 `ruff>=0.16`，并新增 `[tool.ruff]`/`[tool.ruff.lint]`
  配置（`line-length = 120` 以容纳真实浏览器 UA 示例字符串、排除 `*.md` 以保留 README
  代码示例的对齐排版、忽略中文注释触发的 `RUF001-003` 与常量数据类属性触发的
  `RUF012`），使 `ruff check .` / `ruff format --check .` 可正常运行。

### 修复

- README 的 Python 版本徽章由 `3.8+` 更正为 `3.10+`，与 `pyproject.toml` 的
  `requires-python = ">=3.10"` 保持一致。
- `pyproject.toml` 补充 `[project] license = "MIT"` 声明，并将
  `[tool.setuptools] license-files` 指向 `LICENSE`。
- 停止跟踪 `uv.lock`；作为库项目，不在版本控制中维护该锁文件。
- 接入 Ruff 后修复了既有的真实 lint 问题：移除 `headers/browsers.py` 中未使用的
  `randint as rint` 导入、为 `base.py` 中 3 处 `zip(*weighted_names)` 补充
  `strict=True`（解包同长度的 `(name, weight)` 元组列表，显式声明长度不变式）、
  将一处 `if/else` 赋值简化为三元表达式，并对全部源码跑了 `ruff format .`
  （仅限 `.py` 文件，`*.md` 已排除）。

### 变更

- `src/funfake/base.py`、`src/funfake/phones/core.py`、`src/funfake/names/core.py`、
  `src/funfake/names/scenarios.py` 中的类型标注由 `typing.Optional`/`List`/`Dict`/`Tuple`
  改为 Python 3.10 原生写法（`X | None`、`list[...]`、`dict[...]`、`tuple[...]`）。
- README 末尾追加组织统一介绍区块。
- `.gitignore` 补充 `*.db`、`*.rar`、`.run/`、`logs/`、`.vscode/`。

### 废弃

- 无。

## [1.1.6]

### 新增

- 无。

### 修复

- 修正 README 中 Linux 平台参数示例，并补充请求头 API 文档。

### 变更

- 无。

### 废弃

- 无。
