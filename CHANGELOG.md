# CHANGELOG

本文件记录 funfake 的版本变更，按版本倒序排列。

## [1.1.6]

### 新增

- 无。

### 修复

- 修正 README 中 Linux 平台参数示例，并补充请求头 API 文档。

### 变更

- 无。

### 废弃

- 无。

## [未发布]

### 新增

- 新增根目录 `CHANGELOG.md`。
- 补充 `tests/test_smoke.py` 对公开 API 边界/非法参数场景的覆盖：`fake_name`/`fake_phone`
  非法参数、`Headers.empty()`、`headers.headers.make_header()`。

### 修复

- README 的 Python 版本徽章由 `3.8+` 更正为 `3.10+`，与 `pyproject.toml` 的
  `requires-python = ">=3.10"` 保持一致。
- `pyproject.toml` 补充 `[project] license = "MIT"` 声明，并将
  `[tool.setuptools] license-files` 指向 `LICENSE`。
- 补充并提交 `uv.lock`，保证可复现构建。

### 变更

- `src/funfake/base.py`、`src/funfake/phones/core.py`、`src/funfake/names/core.py`、
  `src/funfake/names/scenarios.py` 中的类型标注由 `typing.Optional`/`List`/`Dict`/`Tuple`
  改为 Python 3.10 原生写法（`X | None`、`list[...]`、`dict[...]`、`tuple[...]`）。
- README 末尾追加组织统一介绍区块。
- `.gitignore` 补充 `*.db`、`*.rar`、`.run/`、`logs/`、`.vscode/`。

### 废弃

- 无。
