"""
headers - HTTP 请求头生成模块

该模块提供了真实的 HTTP 请求头生成功能，支持多种浏览器和操作系统的模拟。

主要组件：
- Headers: 可配置的 HTTP 请求头生成器类
- fake_header: 快速生成随机请求头的便捷函数

Example:
    >>> from funfake.headers import fake_header, Headers
    >>> 
    >>> # 快速生成随机请求头
    >>> headers = fake_header()
    >>> 
    >>> # 自定义浏览器和操作系统
    >>> gen = Headers(browser='chrome', os='win', headers=True)
    >>> headers = gen.generate()
"""

from .core import Headers, fake_header

__all__ = ["Headers", "fake_header"]
