"""
names - 姓名生成模块

该模块提供了多种类型的姓名生成功能，包括：
- 通用姓名生成器（中文、英文）
- 场景化姓名生成器（基于经典文学作品）

支持的场景：
- 水浒传、西游记、红楼梦
- 三国演义、封神演义
- 金庸武侠系列

Example:
    >>> from funfake.names import fake_name, WaterMarginName
    >>> 
    >>> # 快速生成随机姓名
    >>> name = fake_name('chinese')
    >>> 
    >>> # 生成水浒传人物姓名
    >>> gen = WaterMarginName()
    >>> name = gen.generate(group="正派")
"""

from .core import ChineseName, EnglishName, fake_name
from .scenarios import (
    DreamOfRedChamberName,
    InvestitureOfGodsName,
    JinYongWuxiaName,
    JourneyToWestName,
    RomanceOfThreeKingdomsName,
    WaterMarginName,
)

__all__ = [
    "ChineseName",
    "EnglishName",
    "WaterMarginName",
    "JourneyToWestName",
    "DreamOfRedChamberName",
    "RomanceOfThreeKingdomsName",
    "InvestitureOfGodsName",
    "JinYongWuxiaName",
    "fake_name",
]
