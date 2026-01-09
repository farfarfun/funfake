"""
HTTP 请求头生成核心模块。

该模块提供了 Headers 类和 fake_header 函数，用于生成真实的 HTTP 请求头信息。
"""

from ..base import BaseGenerator
from .browsers import chrome, firefox, opera, random_browser
from .headers import make_header
from .platforms import linux, macos, random_os, windows


class Headers(BaseGenerator):
    """
    HTTP 请求头生成器。
    
    支持自定义浏览器类型、操作系统和额外的 HTTP 头信息，用于模拟真实的浏览器请求。
    
    Args:
        browser: 浏览器类型，可选值：
                - 'chrome': Chrome 浏览器
                - 'firefox': Firefox 浏览器
                - 'opera': Opera 浏览器
                - None: 随机选择（默认）
        os: 操作系统类型，可选值：
                - 'win': Windows 系统
                - 'mac': macOS 系统
                - 'lin': Linux 系统
                - None: 随机选择（默认）
        headers: 是否生成额外的 HTTP 头信息，默认为 False
                - True: 包含 Accept-Encoding、Accept-Language、Referer 等额外头信息
                - False: 只生成基础头信息（Accept、Connection、User-Agent）
    
    Example:
        >>> # 生成 Chrome + Windows 的请求头
        >>> gen = Headers(browser='chrome', os='win', headers=True)
        >>> headers = gen.generate()
        >>> print(headers['User-Agent'])
        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...
    """

    # 操作系统映射表
    __os = {"win": windows, "mac": macos, "lin": linux}

    # 浏览器映射表
    __browser = {"chrome": chrome, "firefox": firefox, "opera": opera}

    def __init__(self, browser: str = None, os: str = None, headers: bool = False):
        """
        初始化 HTTP 请求头生成器。
        
        Args:
            browser: 浏览器类型，默认为 None（随机选择）
            os: 操作系统类型，默认为 None（随机选择）
            headers: 是否生成额外的 HTTP 头信息，默认为 False
        """
        self.__platform = self.__os.get(os, random_os)
        self.__browser = self.__browser.get(browser, random_browser)
        self.__headers = make_header if headers else self.empty

    def empty(self) -> dict:
        """
        返回空字典（用于不需要额外头信息的情况）。
        
        Returns:
            dict: 空字典
        """
        return {}

    def generate(self) -> dict:
        """
        生成 HTTP 请求头字典。
        
        Returns:
            dict: 包含 HTTP 请求头的字典，至少包含以下键：
                 - Accept: 接受的内容类型
                 - Connection: 连接类型
                 - User-Agent: 用户代理字符串
                 如果 headers=True，还会包含额外的头信息（如 Accept-Encoding、Referer 等）
                 
        Example:
            >>> gen = Headers(browser='chrome', os='win')
            >>> headers = gen.generate()
            >>> print(headers.keys())
            dict_keys(['Accept', 'Connection', 'User-Agent'])
        """
        # 生成平台和浏览器信息
        platform = self.__platform()
        browser = self.__browser()

        # 构建基础请求头
        headers = {
            "Accept": "*/*",
            "Connection": "keep-alive",
            "User-Agent": browser.replace("%PLAT%", platform),  # 替换占位符
        }

        # 添加额外的请求头（如果启用）
        headers.update(self.__headers())

        return headers


# 全局单例，用于快速生成随机请求头
__headers = Headers()


def fake_header() -> dict:
    """
    快速生成随机的 HTTP 请求头。
    
    这是一个便捷函数，使用默认配置（随机浏览器、随机操作系统、不包含额外头信息）
    生成 HTTP 请求头。
    
    Returns:
        dict: 包含随机 HTTP 请求头的字典
        
    Example:
        >>> from funfake import fake_header
        >>> headers = fake_header()
        >>> print(headers['User-Agent'])
        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...
    """
    return __headers.generate()
