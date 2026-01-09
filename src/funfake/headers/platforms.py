"""
操作系统平台信息生成模块。

该模块提供了常见操作系统的平台信息字符串生成功能，用于构建完整的 User-Agent。
支持的操作系统：
- Windows: Windows NT 6.0-10.0，支持 WOW64 和 Win64; x64 架构
- macOS: Mac OS X 10.10-10.14
- Linux: 支持 x86_64、i686 架构
"""

import random
from random import randint as rint


def windows() -> str:
    """
    生成 Windows 操作系统的平台信息字符串。
    
    Returns:
        str: Windows 平台信息，格式如 "Windows NT 10.0; Win64; x64" 或 "Windows NT 6.1"
        
    Example:
        >>> platform = windows()
        >>> print(platform)
        Windows NT 10.0; WOW64
    """
    etc = ["WOW64", "Win64; x64"]  # 架构标识
    ver = ["10.0", f"6.{rint(0, 3)}"]  # 版本号：10.0 或 6.0-6.3
    main = "Windows NT "

    version = random.choice(ver)

    # Windows 10.0 或随机情况下添加架构信息
    if version == "10.0" or rint(0, 1):
        version += f"; {random.choice(etc)}"

    return main + version


def macos() -> str:
    """
    生成 macOS 操作系统的平台信息字符串。
    
    Returns:
        str: macOS 平台信息，格式如 "Macintosh; Intel Mac OS X 10_14_2"
        
    Example:
        >>> platform = macos()
        >>> print(platform)
        Macintosh; Intel Mac OS X 10_13_4
    """
    main = "Macintosh; Intel Mac OS X 10_"
    # 主版本号：10.10 到 10.14
    sub = str(rint(10, 14))
    # 次版本号：最高为 6，但 10.14 最高为 2
    sub += "_" + str(rint(1, (6 if sub != "14" else 2)))

    return main + sub


def linux() -> str:
    """
    生成 Linux 操作系统的平台信息字符串。
    
    Returns:
        str: Linux 平台信息，格式如 "X11; Linux x86_64"
        
    Example:
        >>> platform = linux()
        >>> print(platform)
        X11; Linux x86_64
    """
    ver = ["x86_64", "i686", "i686 on x86_64"]  # 架构类型
    main = "X11; Linux "

    return main + random.choice(ver)


def random_os() -> str:
    """
    随机选择一个操作系统并生成其平台信息字符串。
    
    从 Windows、macOS、Linux 中随机选择一个操作系统。
    
    Returns:
        str: 随机操作系统的平台信息
        
    Example:
        >>> platform = random_os()
        >>> # 可能返回 Windows、macOS 或 Linux 的平台信息
    """
    os_functions = [windows, macos, linux]
    return random.choice(os_functions)()
