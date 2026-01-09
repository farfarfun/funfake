"""
funfake - 轻量级的 Python 伪造数据生成库

该库提供了真实的 HTTP 请求头、各类姓名和手机号码生成功能，
帮助模拟各种浏览器、操作系统和用户身份。

主要功能模块：
- headers: HTTP 请求头生成（支持 Chrome、Firefox、Opera 等浏览器）
- names: 姓名生成（支持中文、英文和经典文学作品人物姓名）
- phones: 手机号码生成（支持中国和美国手机号）

快速开始：
    >>> from funfake import fake_header, fake_name, fake_phone
    >>> 
    >>> # 生成 HTTP 请求头
    >>> headers = fake_header()
    >>> 
    >>> # 生成随机姓名
    >>> name = fake_name()
    >>> 
    >>> # 生成随机手机号
    >>> phone = fake_phone()

详细文档请参考：https://github.com/farfarfun/funfake
"""

from .base import BaseGenerator, ListBasedGenerator
from .headers import Headers, fake_header
from .names import (
    ChineseName,
    DreamOfRedChamberName,
    EnglishName,
    InvestitureOfGodsName,
    JinYongWuxiaName,
    JourneyToWestName,
    RomanceOfThreeKingdomsName,
    WaterMarginName,
    fake_name,
)
from .phones import ChinesePhone, EnglishPhone, fake_phone

__all__ = [
    "BaseGenerator",
    "ListBasedGenerator",
    "fake_header",
    "Headers",
    "ChineseName",
    "EnglishName",
    "WaterMarginName",
    "JourneyToWestName",
    "DreamOfRedChamberName",
    "RomanceOfThreeKingdomsName",
    "InvestitureOfGodsName",
    "JinYongWuxiaName",
    "fake_name",
    "ChinesePhone",
    "EnglishPhone",
    "fake_phone",
]
