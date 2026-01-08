# funfake

[![PyPI version](https://badge.fury.io/py/funfake.svg)](https://badge.fury.io/py/funfake)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

一个轻量级的Python库，用于生成真实的HTTP请求头、各类姓名和手机号码，帮助模拟各种浏览器、操作系统和用户身份。

## ✨ 特性

### HTTP 请求头生成
- 🎭 **真实模拟**: 支持Chrome、Firefox、Opera等主流浏览器
- 🖥️ **多平台**: 支持Windows、macOS、Linux操作系统
- 🎲 **随机生成**: 智能随机组合生成逼真的请求头
- 🚀 **零依赖**: 纯Python实现，无外部依赖
- 📦 **轻量级**: 简单易用的API设计
- 🔄 **高度可定制**: 支持指定特定浏览器和操作系统

### 姓名生成
- 👤 **多语言支持**: 支持中文姓名和英文姓名生成
- 📚 **经典文学**: 支持水浒传、西游记、红楼梦、三国演义、封神演义、金庸武侠等经典作品人物姓名
- 🎯 **分组功能**: 支持按正派/反派、势力、作品等维度分组生成
- ⚖️ **概率权重**: 支持为不同分组设置出现概率，更真实地模拟分布
- 🔢 **批量生成**: 支持一次生成多个不重复的姓名

### 手机号码生成
- 📱 **多国支持**: 支持中国和美国手机号码生成
- 🏢 **运营商支持**: 中国手机号支持移动、联通、电信三大运营商
- ⚖️ **概率权重**: 支持为不同运营商设置出现概率（移动用户最多）
- 🔢 **批量生成**: 支持一次生成多个不重复的手机号码
- 📐 **格式灵活**: 美国手机号支持带/不带连字符格式

## 📦 安装

```bash
pip install funfake
```

## 🚀 快速开始

### HTTP 请求头生成

#### 基础用法

```python
from funfake import fake_header

# 生成随机请求头
headers = fake_header()
print(headers)
# 输出示例:
# {
#     'Accept': '*/*',
#     'Connection': 'keep-alive',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US;q=0.5,en;q=0.3',
#     'Referer': 'https://www.google.com'
# }
```

#### 高级用法

```python
from funfake import Headers

# 指定浏览器和操作系统
chrome_headers = Headers(browser='chrome', os='win', headers=True)
headers = chrome_headers.generate()

# 指定Firefox浏览器，macOS系统
firefox_headers = Headers(browser='firefox', os='mac', headers=True)
headers = firefox_headers.generate()

# 只生成基础请求头（不包含额外头信息）
basic_headers = Headers(browser='chrome', os='lin', headers=False)
headers = basic_headers.generate()

# 生成多个不重复的请求头
multiple_headers = Headers().generate_many(5)
```

### 姓名生成

#### 基础用法

```python
from funfake import fake_name, ChineseName, EnglishName

# 快速生成随机姓名
name = fake_name()  # 随机选择中文或英文
name = fake_name('chinese')  # 生成中文姓名
name = fake_name('english')  # 生成英文姓名

# 使用生成器类
chinese = ChineseName()
name = chinese.generate()  # 例如: "王伟"

english = EnglishName()
name = english.generate()  # 例如: "John Smith"

# 生成多个不重复的姓名
chinese_names = chinese.generate_many(10)  # 生成10个不重复的中文姓名
english_names = english.generate_many(10)  # 生成10个不重复的英文姓名
```

#### 场景类姓名生成

```python
from funfake import (
    WaterMarginName,        # 水浒传
    JourneyToWestName,      # 西游记
    DreamOfRedChamberName,  # 红楼梦
    RomanceOfThreeKingdomsName,  # 三国演义
    InvestitureOfGodsName,  # 封神演义
    JinYongWuxiaName,       # 金庸武侠
)

# 生成水浒传人物姓名
water_margin = WaterMarginName()
name = water_margin.generate()  # 例如: "林冲"

# 查看可用分组
groups = water_margin.get_groups()  # ['正派', '反派']

# 从指定组生成（正派/反派）
name = water_margin.generate(group="正派")  # 只生成正派人物
name = water_margin.generate(group="反派")  # 只生成反派人物

# 生成多个不重复的姓名
names = water_margin.generate_many(5, group="正派")  # 生成5个正派人物

# 三国演义 - 按势力分组
three_kingdoms = RomanceOfThreeKingdomsName()
groups = three_kingdoms.get_groups()  # ['蜀汉', '曹魏', '东吴', '其他']
name = three_kingdoms.generate(group="蜀汉")  # 只生成蜀汉人物

# 西游记 - 按正派/反派/中立分组
journey = JourneyToWestName()
name = journey.generate(group="正派")  # 生成正派人物（如：孙悟空、观音菩萨）
name = journey.generate(group="反派")  # 生成反派人物（如：牛魔王、白骨精）
```

#### 概率权重

场景类生成器支持概率权重，不同分组有不同的出现概率：

```python
water_margin = WaterMarginName()
# 正派权重: 10.0，反派权重: 1.0
# 生成时正派人物出现概率更高
name = water_margin.generate()  # 更可能生成正派人物
```

### 手机号码生成

#### 基础用法

```python
from funfake import fake_phone, ChinesePhone, EnglishPhone

# 快速生成随机手机号
phone = fake_phone()  # 随机选择中国或美国
phone = fake_phone('chinese')  # 生成中国手机号
phone = fake_phone('english')  # 生成美国手机号

# 使用生成器类
chinese_phone = ChinesePhone()
phone = chinese_phone.generate()  # 例如: "13812345678"

english_phone = EnglishPhone()
phone = english_phone.generate()  # 例如: "555-123-4567"

# 生成多个不重复的手机号
phones = chinese_phone.generate_many(10)  # 生成10个不重复的中国手机号
```

#### 中国手机号 - 运营商支持

```python
from funfake import ChinesePhone

chinese_phone = ChinesePhone()

# 查看可用运营商
operators = chinese_phone.get_operators()  # ['移动', '联通', '电信']

# 从指定运营商生成
phone = chinese_phone.generate(operator="移动")  # 只生成移动号码
phone = chinese_phone.generate(operator="联通")  # 只生成联通号码
phone = chinese_phone.generate(operator="电信")  # 只生成电信号码

# 生成多个不重复的手机号
phones = chinese_phone.generate_many(10, operator="移动")  # 生成10个移动号码

# 按运营商权重随机生成（移动权重最高）
phone = chinese_phone.generate()  # 更可能生成移动号码
```

#### 美国手机号 - 格式支持

```python
from funfake import EnglishPhone

english_phone = EnglishPhone()

# 带连字符格式（默认）
phone = english_phone.generate()  # 例如: "555-123-4567"

# 不带连字符格式
phone = english_phone.generate(format_with_dash=False)  # 例如: "5551234567"

# 初始化时设置格式
phone_gen = EnglishPhone(format_with_dash=False)
phone = phone_gen.generate()  # 始终生成不带连字符的格式
```

## 📚 API 文档

### HTTP 请求头生成

#### `fake_header()`

生成随机的HTTP请求头。

**返回值**: `dict` - 包含HTTP请求头的字典

#### `Headers` 类

用于自定义生成HTTP请求头的类。

**参数**:
- `browser` (str, 可选): 浏览器类型
  - `'chrome'`: Chrome浏览器
  - `'firefox'`: Firefox浏览器  
  - `'opera'`: Opera浏览器
  - `None`: 随机选择 (默认)

- `os` (str, 可选): 操作系统类型
  - `'win'`: Windows系统
  - `'mac'`: macOS系统
  - `'lin'`: Linux系统
  - `None`: 随机选择 (默认)

- `headers` (bool, 可选): 是否生成额外的HTTP头
  - `True`: 包含Accept-Encoding、Accept-Language等额外头信息
  - `False`: 只包含基础头信息 (默认)

**方法**:
- `generate()`: 生成HTTP请求头字典
- `generate_many(count, allow_duplicates=False)`: 生成多个不重复的请求头

### 姓名生成

#### `fake_name(language=None)`

快速生成随机姓名。

**参数**:
- `language` (str, 可选): 语言类型
  - `'chinese'`: 生成中文姓名
  - `'english'`: 生成英文姓名
  - `None`: 随机选择 (默认)

**返回值**: `str` - 生成的姓名

#### `ChineseName` 类

中文姓名生成器。

**参数**:
- `double_name_probability` (float, 可选): 生成双字名字的概率，默认 0.3

**方法**:
- `generate()`: 生成单个中文姓名
- `generate_many(count, allow_duplicates=False)`: 生成多个不重复的中文姓名

#### `EnglishName` 类

英文姓名生成器。

**方法**:
- `generate()`: 生成单个英文姓名
- `generate_many(count, allow_duplicates=False)`: 生成多个不重复的英文姓名

#### 场景类姓名生成器

所有场景类生成器都继承自 `ListBasedGenerator`，支持以下功能：

**类列表**:
- `WaterMarginName`: 水浒传
- `JourneyToWestName`: 西游记
- `DreamOfRedChamberName`: 红楼梦
- `RomanceOfThreeKingdomsName`: 三国演义
- `InvestitureOfGodsName`: 封神演义
- `JinYongWuxiaName`: 金庸武侠

**方法**:
- `generate(group=None)`: 生成单个姓名
  - `group` (str, 可选): 指定分组，如 "正派"、"反派" 等
- `generate_many(count, allow_duplicates=False, group=None)`: 生成多个不重复的姓名
  - `count` (int): 要生成的数量
  - `allow_duplicates` (bool): 是否允许重复（当数量超过可用数据时）
  - `group` (str, 可选): 指定分组
- `get_groups()`: 获取所有可用的分组列表

### 基类

#### `BaseGenerator` 类

所有生成器的抽象基类。

**方法**:
- `generate()`: 抽象方法，子类必须实现
- `generate_many(count, allow_duplicates=False)`: 生成多个不重复的结果（默认实现）

#### `ListBasedGenerator` 类

基于固定列表的生成器基类，支持概率权重和分组。

**配置方式**:
- `NAMES`: 简单列表（向后兼容）
- `NAMES_BY_GROUP`: 按组分组的名字字典（推荐）
- `GROUP_WEIGHTS`: 组的权重字典，控制不同组的出现概率

### 手机号码生成

#### `fake_phone(country=None)`

快速生成随机手机号码。

**参数**:
- `country` (str, 可选): 国家类型
  - `'chinese'`: 生成中国手机号
  - `'english'`: 生成美国手机号
  - `None`: 随机选择 (默认)

**返回值**: `str` - 生成的手机号码

#### `ChinesePhone` 类

中国手机号码生成器。

**参数**:
- `operator` (str, 可选): 运营商类型，'移动'/'联通'/'电信'，None 表示按权重随机选择

**方法**:
- `generate(operator=None)`: 生成单个中国手机号（11位）
  - `operator` (str, 可选): 临时指定运营商
- `generate_many(count, allow_duplicates=False, operator=None)`: 生成多个不重复的中国手机号
- `get_operators()`: 获取所有可用的运营商列表

**运营商权重**:
- 移动: 10.0（用户最多）
- 联通: 6.0
- 电信: 4.0

#### `EnglishPhone` 类

美国手机号码生成器。

**参数**:
- `format_with_dash` (bool, 可选): 是否使用连字符格式化，默认 True

**方法**:
- `generate(format_with_dash=None)`: 生成单个美国手机号
  - `format_with_dash` (bool, 可选): 是否使用连字符（XXX-XXX-XXXX 或 XXXXXXXXXX）
- `generate_many(count, allow_duplicates=False, format_with_dash=None)`: 生成多个不重复的美国手机号

## 🎯 使用场景

### HTTP 请求头生成
- **Web爬虫**: 避免被网站检测为机器人
- **API测试**: 模拟真实用户请求
- **负载测试**: 生成多样化的请求头
- **浏览器兼容性测试**: 测试不同浏览器环境
- **网络请求模拟**: 在自动化测试中使用

### 姓名生成
- **测试数据生成**: 为测试用例生成随机姓名
- **游戏开发**: 生成NPC角色姓名
- **数据脱敏**: 生成假姓名替换真实数据
- **内容创作**: 为小说、游戏等生成角色姓名
- **用户注册测试**: 批量生成测试用户姓名

### 手机号码生成
- **测试数据生成**: 为测试用例生成随机手机号
- **用户注册测试**: 批量生成测试用户手机号
- **数据脱敏**: 生成假手机号替换真实数据
- **API测试**: 模拟用户手机号进行接口测试
- **负载测试**: 生成大量不重复的手机号进行压力测试

## 📊 支持的浏览器版本

| 浏览器 | 支持版本数量 | 版本范围 |
|--------|-------------|----------|
| Chrome | 66 | 60 - 87 |
| Firefox | 134 | 50 - 80 |
| Opera | 41 | 50 - 67 |

## 🖥️ 支持的操作系统

- **Windows**: Windows NT 6.0-6.3, Windows 10
- **macOS**: Mac OS X 10.10-10.14
- **Linux**: 支持x86_64、i686架构

## 🌐 真实引用域名

内置500个真实网站域名作为Referer，包括：
- Google、YouTube、Facebook等主流网站
- 各国Wikipedia、新闻媒体网站
- 技术类网站如GitHub、Stack Overflow
- 电商网站如Amazon、eBay

## 👤 支持的姓名类型

### 基础姓名生成器

| 类型 | 说明 | 数据量 |
|------|------|--------|
| 中文姓名 | 常见中文姓氏 + 名字 | 100+ 姓氏，100+ 名字 |
| 英文姓名 | 常见英文名字 + 姓氏 | 200+ 名字，200+ 姓氏 |

### 场景类姓名生成器

| 场景 | 分组维度 | 数据量 |
|------|---------|--------|
| 水浒传 | 正派/反派 | 108+ 人物 |
| 西游记 | 正派/反派/中立 | 60+ 人物 |
| 红楼梦 | 主要角色/次要角色/丫鬟 | 100+ 人物 |
| 三国演义 | 蜀汉/曹魏/东吴/其他 | 150+ 人物 |
| 封神演义 | 阐教/截教/商朝/周朝/其他 | 100+ 人物 |
| 金庸武侠 | 按作品分组（7个作品） | 200+ 人物 |

### 分组和权重示例

**水浒传**:
- 正派: 权重 10.0（108个梁山好汉）
- 反派: 权重 1.0（高俅、蔡京等）

**西游记**:
- 正派: 权重 8.0（孙悟空、观音菩萨等）
- 反派: 权重 5.0（牛魔王、白骨精等）
- 中立: 权重 2.0（土地、山神等）

**三国演义**:
- 蜀汉: 权重 8.0
- 曹魏: 权重 8.0
- 东吴: 权重 8.0
- 其他: 权重 3.0

## 📱 支持的手机号码格式

### 中国手机号

| 运营商 | 号段前缀 | 权重 | 说明 |
|--------|---------|------|------|
| 移动 | 134-139, 147, 150-152, 157-159, 178, 182-184, 187-188, 198 | 10.0 | 用户最多 |
| 联通 | 130-132, 145, 155-156, 166, 171, 175-176, 185-186 | 6.0 | 第二大运营商 |
| 电信 | 133, 149, 153, 173, 177, 180-181, 189, 199 | 4.0 | 第三大运营商 |

**格式**: 11位数字，1开头

### 美国手机号

**格式**: 10位数字，支持两种格式
- 带连字符: `XXX-XXX-XXXX` (12个字符)
- 不带连字符: `XXXXXXXXXX` (10个字符)

**区号规则**: 前3位不能以0或1开头，支持200+个真实区号

## 🔧 实际应用示例

### HTTP 请求头生成

#### 在requests中使用

```python
import requests
from funfake import fake_header

url = "https://httpbin.org/headers"
headers = fake_header()

response = requests.get(url, headers=headers)
print(response.json())
```

#### 在爬虫中使用

```python
import requests
from funfake import Headers

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.header_generator = Headers(headers=True)
    
    def get_page(self, url):
        # 每次请求使用不同的请求头
        headers = self.header_generator.generate()
        self.session.headers.update(headers)
        return self.session.get(url)
```

### 姓名生成

#### 批量生成测试用户

```python
from funfake import ChineseName, EnglishName

# 生成100个中文测试用户姓名
chinese = ChineseName()
users = chinese.generate_many(100)
for i, name in enumerate(users, 1):
    print(f"用户{i}: {name}")
```

#### 游戏角色生成

```python
from funfake import WaterMarginName, JourneyToWestName

# 生成水浒传正派角色
water_margin = WaterMarginName()
heroes = water_margin.generate_many(10, group="正派")
villains = water_margin.generate_many(5, group="反派")

print("正派角色:", heroes)
print("反派角色:", villains)
```

#### 按概率生成角色

```python
from funfake import JourneyToWestName

journey = JourneyToWestName()

# 生成100个角色，正派权重更高，会出现更多正派角色
characters = []
for _ in range(100):
    characters.append(journey.generate())

# 统计分布
from collections import Counter
counter = Counter(characters)
# 正派角色（如孙悟空、观音菩萨）出现频率会更高
```

#### 多维度分组生成

```python
from funfake import RomanceOfThreeKingdomsName

three_kingdoms = RomanceOfThreeKingdomsName()

# 按势力生成角色
shu_heroes = three_kingdoms.generate_many(10, group="蜀汉")
wei_heroes = three_kingdoms.generate_many(10, group="曹魏")
wu_heroes = three_kingdoms.generate_many(10, group="东吴")

print("蜀汉:", shu_heroes)
print("曹魏:", wei_heroes)
print("东吴:", wu_heroes)
```

### 手机号码生成

#### 批量生成测试用户手机号

```python
from funfake import ChinesePhone, EnglishPhone

# 生成100个中国手机号
chinese_phone = ChinesePhone()
phones = chinese_phone.generate_many(100)
for i, phone in enumerate(phones, 1):
    print(f"用户{i}: {phone}")
```

#### 按运营商生成

```python
from funfake import ChinesePhone

chinese_phone = ChinesePhone()

# 生成移动号码
mobile_phones = chinese_phone.generate_many(10, operator="移动")

# 生成联通号码
unicom_phones = chinese_phone.generate_many(10, operator="联通")

# 生成电信号码
telecom_phones = chinese_phone.generate_many(10, operator="电信")
```

#### 按概率生成（移动用户更多）

```python
from funfake import ChinesePhone

chinese_phone = ChinesePhone()

# 生成100个手机号，移动权重更高，会出现更多移动号码
phones = []
for _ in range(100):
    phones.append(chinese_phone.generate())

# 统计运营商分布
from collections import Counter
# 移动号码会更多（权重10.0 vs 联通6.0 vs 电信4.0）
```

#### 不同格式的美国手机号

```python
from funfake import EnglishPhone

# 带连字符格式（默认）
phone_gen1 = EnglishPhone(format_with_dash=True)
phone1 = phone_gen1.generate()  # "555-123-4567"

# 不带连字符格式
phone_gen2 = EnglishPhone(format_with_dash=False)
phone2 = phone_gen2.generate()  # "5551234567"
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👥 作者

- **牛哥** - [niuliangtao@qq.com](mailto:niuliangtao@qq.com)
- **farfarfun团队** - [farfarfun@qq.com](mailto:farfarfun@qq.com)

## 🔗 相关链接

- [GitHub仓库](https://github.com/farfarfun/funfake)
- [PyPI包](https://pypi.org/project/funfake/)
- [发布页面](https://github.com/farfarfun/funfake/releases)
- [组织主页](https://github.com/farfarfun)