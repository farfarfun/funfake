
# Headers Module

funfake库的核心模块，用于生成真实的HTTP请求头信息。

## 📁 模块结构

```
headers/
├── __init__.py      # 模块入口，导出主要API
├── core.py          # Headers类和fake_header函数
├── browsers.py      # 浏览器User-Agent生成器
├── platforms.py     # 操作系统平台信息生成器
├── headers.py       # HTTP头信息和域名数据
└── README.md        # 本文档
```

## 🔧 核心组件

### 1. Headers类 (`core.py`)

主要的请求头生成类，支持自定义配置。

```python
from funfake.headers import Headers

# 创建Headers实例
headers_gen = Headers(
    browser='chrome',    # 浏览器类型: chrome/firefox/opera/None(随机)
    os='win',           # 操作系统: win/mac/lin/None(随机)
    headers=True        # 是否生成额外HTTP头: True/False
)

# 生成请求头
headers = headers_gen.generate()
```

### 2. 浏览器模拟器 (`browsers.py`)

支持三种主流浏览器的User-Agent生成：

- **Chrome**: 71个版本，从50.0到87.0
- **Firefox**: 138个版本，从50.0到80.0
- **Opera**: 42个版本，从50.0到67.0

```python
from funfake.headers.browsers import chrome, firefox, opera, random_browser

# 生成特定浏览器User-Agent
chrome_ua = chrome()
firefox_ua = firefox()
opera_ua = opera()

# 随机选择浏览器
random_ua = random_browser()
```

### 3. 平台信息生成器 (`platforms.py`)

生成真实的操作系统平台信息：

```python
from funfake.headers.platforms import windows, macos, linux, random_os

# 生成特定平台信息
win_platform = windows()    # Windows NT 6.0-10.0
mac_platform = macos()     # Mac OS X 10.10-10.14
linux_platform = linux()   # Linux x86_64/i686

# 随机选择平台
random_platform = random_os()
```

### 4. HTTP头生成器 (`headers.py`)

生成额外的HTTP头信息和引用域名：

```python
from funfake.headers.headers import make_header

# 生成随机HTTP头
extra_headers = make_header()
# 可能包含: Accept-Encoding, Accept-Language, Cache-Control等
```

## 🎯 快速使用

### 基础用法

```python
from funfake import fake_header

# 一键生成随机请求头
headers = fake_header()
print(headers)
```

### 高级定制

```python
from funfake import Headers

# Chrome + Windows + 完整头信息
chrome_win = Headers(browser='chrome', os='win', headers=True)
headers = chrome_win.generate()

# Firefox + macOS + 基础头信息
firefox_mac = Headers(browser='firefox', os='mac', headers=False)
headers = firefox_mac.generate()

# 完全随机
random_headers = Headers()
headers = random_headers.generate()
```

## 📊 数据统计

| 组件 | 数据量 | 说明 |
|------|--------|------|
| Chrome版本 | 71个 | 涵盖主流版本号 |
| Firefox版本 | 138个 | 包含ESR和常规版本 |
| Opera版本 | 42个 | 基于Chromium的版本 |
| 引用域名 | 532个 | 真实网站域名 |
| Windows版本 | 动态生成 | NT 6.0-10.0 |
| macOS版本 | 动态生成 | 10.10-10.14 |
| Linux架构 | 3种 | x86_64, i686等 |

## 🔍 生成示例

### 完整请求头示例

```json
{
    "Accept": "*/*",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US;q=0.5,en;q=0.3",
    "Cache-Control": "max-age=0",
    "DNT": "1",
    "Referer": "https://www.google.com",
    "Pragma": "no-cache"
}
```

### User-Agent示例

```
# Chrome
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36

# Firefox  
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2; rv:78.0) Gecko/20100101 Firefox/78.0

# Opera
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.64
```

## ⚡ 性能优化

模块经过性能优化，主要改进：

- 使用`random.choice()`替代手动索引计算
- 字典推导式减少多次update操作
- f-string提升字符串格式化性能
- 减少不必要的函数调用

## 🔧 扩展开发

### 添加新浏览器

```python
def new_browser() -> str:
    versions = ["1.0", "2.0", "3.0"]
    template = "NewBrowser/%VER%"
    return template.replace("%VER%", random.choice(versions))
```

### 添加新平台

```python
def new_platform() -> str:
    return "NewOS 1.0; Architecture"
```

## 🌐 引用域名

内置532个真实网站域名，包括：

- **搜索引擎**: Google, Bing, Yahoo等
- **社交媒体**: Facebook, Twitter, LinkedIn等  
- **技术网站**: GitHub, Stack Overflow, Mozilla等
- **新闻媒体**: BBC, CNN, Reuters等
- **电商平台**: Amazon, eBay, Alibaba等

## 🤝 贡献指南

欢迎贡献新的浏览器版本、平台信息或域名数据：

1. Fork项目
2. 创建特性分支
3. 添加新数据或功能
4. 提交Pull Request

## 📄 许可证

本模块遵循项目整体的MIT许可证。

## 🙏 致谢

感谢以下项目的启发：
- [Fake-Headers](https://github.com/diwu1989/Fake-Headers) - 原始灵感来源
