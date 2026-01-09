"""
phones - 手机号码生成模块

该模块提供了中国和美国手机号码的生成功能。

支持特性：
- 中国手机号：11位，支持移动、联通、电信三大运营商
- 美国手机号：10位，支持带/不带连字符格式
- 运营商权重控制（模拟真实市场份额）
- 批量生成不重复号码

Example:
    >>> from funfake.phones import fake_phone, ChinesePhone
    >>> 
    >>> # 快速生成随机手机号
    >>> phone = fake_phone('chinese')
    >>> 
    >>> # 生成指定运营商的手机号
    >>> gen = ChinesePhone()
    >>> phone = gen.generate(operator="移动")
"""

from .core import ChinesePhone, EnglishPhone, fake_phone

__all__ = ["ChinesePhone", "EnglishPhone", "fake_phone"]
