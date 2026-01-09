import random
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple


class BaseGenerator(ABC):
    """
    所有生成器的抽象基类。
    
    所有具体的生成器类（如姓名生成器、手机号生成器、请求头生成器等）都应该继承此类，
    并实现 generate() 方法来定义具体的生成逻辑。
    
    该基类提供了通用的 generate_many() 方法实现，用于批量生成不重复的结果。
    子类可以根据需要重写此方法以优化性能。
    """

    @abstractmethod
    def generate(self) -> Any:
        """
        生成并返回单个结果。
        
        这是一个抽象方法，子类必须实现此方法来定义具体的生成逻辑。

        Returns:
            Any: 生成的结果，具体类型由子类决定（如字符串、字典等）
        """
        pass

    def generate_many(self, count: int, allow_duplicates: bool = False) -> List[Any]:
        """
        批量生成多个结果（默认情况下不包含重复项）。
        
        本方法提供了一个默认实现，通过循环调用 generate() 方法并去重来生成多个结果。
        子类可以根据自身特点重写此方法以提供更高效的批量生成实现。

        Args:
            count: 要生成的数量，必须为正整数
            allow_duplicates: 是否允许结果重复，默认为 False
                            - False: 确保所有结果不重复，如果可用数据不足会抛出异常
                            - True: 允许结果重复，即使可用数据不足也能生成指定数量

        Returns:
            List[Any]: 生成的结果列表，默认不包含重复项（除非 allow_duplicates=True）

        Raises:
            ValueError: 当 count 小于等于 0 时
            ValueError: 当 allow_duplicates=False 且无法生成足够的不重复结果时
            
        Note:
            该方法最多尝试 count * 100 次生成，以避免在数据源有限时陷入无限循环。
        """
        if count <= 0:
            raise ValueError(f"count must be positive, got {count}")

        results = []
        seen = set()
        max_attempts = count * 100  # 防止无限循环：最多尝试 count * 100 次
        attempts = 0

        # 循环调用 generate() 方法并对结果进行去重
        while len(results) < count and attempts < max_attempts:
            attempts += 1
            result = self.generate()

            # 对于可哈希类型（如字符串、数字），直接使用原值作为去重键
            # 对于不可哈希类型（如字典、列表），转换为字符串进行比较
            if isinstance(result, (str, int, float, tuple)):
                result_key = result
            else:
                result_key = str(result)

            # 检查是否重复，如果不重复则添加到结果列表
            if result_key not in seen:
                seen.add(result_key)
                results.append(result)

        # 如果未能生成足够的不重复结果
        if len(results) < count:
            if allow_duplicates:
                # 允许重复时，继续生成直到达到所需数量（可能包含重复项）
                while len(results) < count:
                    results.append(self.generate())
            else:
                # 不允许重复时，抛出异常说明无法生成足够的不重复结果
                raise ValueError(
                    f"Cannot generate {count} unique results. "
                    f"Only {len(results)} unique results were generated. "
                    f"Set allow_duplicates=True to allow duplicates."
                )

        return results


class ListBasedGenerator(BaseGenerator):
    """
    基于固定列表的生成器基类。
    
    该类为基于预定义数据列表的生成器提供了统一的实现框架，支持以下高级功能：
    - 概率权重：不同数据项或分组可以有不同的出现概率
    - 分组管理：数据可以按类别分组（如正派/反派、不同势力等）
    - 灵活配置：支持多种配置方式以满足不同场景需求
    
    配置方式（子类需要定义以下类属性之一）：
    
    1. NAMES: List[str]
       简单列表配置（向后兼容），所有项权重相等
       示例：NAMES = ["张三", "李四", "王五"]
    
    2. NAMES_WITH_WEIGHTS: List[Tuple[str, float]]
       带权重的列表配置，每个项可以有不同的出现概率
       示例：NAMES_WITH_WEIGHTS = [("张三", 2.0), ("李四", 1.0)]
    
    3. NAMES_BY_GROUP: Dict[str, List[str]] (推荐)
       按组分组的配置，支持按类别管理数据
       示例：NAMES_BY_GROUP = {"正派": ["张三", "李四"], "反派": ["王五"]}
       可配合 GROUP_WEIGHTS 设置各组的权重
    
    注意：
        - 子类只能定义上述配置方式之一，不能同时使用多种方式
        - 使用 NAMES_BY_GROUP 时，可以额外定义 GROUP_WEIGHTS 来设置组权重
    """

    # 子类可以定义这些类属性
    NAMES: List[str] = []  # 简单列表（所有项权重相等）
    NAMES_WITH_WEIGHTS: List[Tuple[str, float]] = []  # 带权重的列表
    NAMES_BY_GROUP: Dict[str, List[str]] = {}  # 按组分组的字典
    GROUP_WEIGHTS: Dict[str, float] = {}  # 组权重（仅在使用 NAMES_BY_GROUP 时有效）

    def __init__(self, group: Optional[str] = None):
        """
        初始化基于列表的生成器。

        Args:
            group: 指定要使用的分组名称，仅在子类定义了 NAMES_BY_GROUP 时有效
                  - None: 从所有分组中随机选择（按权重）
                  - str: 只从指定的分组中选择
        """
        self.group = group
        self._validate_config()

    def _validate_config(self) -> None:
        """
        验证子类的配置是否有效。
        
        确保子类只定义了一种配置方式（NAMES、NAMES_WITH_WEIGHTS 或 NAMES_BY_GROUP），
        避免配置冲突导致的不确定行为。
        
        Raises:
            ValueError: 当子类未定义任何配置或定义了多种配置时
        """
        has_names = bool(self.NAMES)
        has_weights = bool(self.NAMES_WITH_WEIGHTS)
        has_groups = bool(self.NAMES_BY_GROUP)

        config_count = sum([has_names, has_weights, has_groups])
        if config_count == 0:
            raise ValueError(
                "Subclass must define at least one of: NAMES, NAMES_WITH_WEIGHTS, or NAMES_BY_GROUP"
            )
        if config_count > 1:
            raise ValueError(
                "Subclass should define only one of: NAMES, NAMES_WITH_WEIGHTS, or NAMES_BY_GROUP"
            )

    def _get_available_names(self) -> List[str]:
        """
        获取当前可用的名字列表。
        
        根据配置方式和分组设置，返回可用于随机选择的名字列表。
        
        Returns:
            List[str]: 可用的名字列表
            
        Raises:
            ValueError: 当指定的分组不存在时
        """
        if self.NAMES_BY_GROUP:
            if self.group:
                # 如果指定了分组，只返回该分组的名字
                if self.group not in self.NAMES_BY_GROUP:
                    raise ValueError(
                        f"Group '{self.group}' not found in NAMES_BY_GROUP"
                    )
                return self.NAMES_BY_GROUP[self.group]
            else:
                # 未指定分组时，返回所有分组的名字（合并）
                all_names = []
                for names in self.NAMES_BY_GROUP.values():
                    all_names.extend(names)
                return all_names
        elif self.NAMES_WITH_WEIGHTS:
            # 从带权重的列表中提取名字部分
            return [name for name, _ in self.NAMES_WITH_WEIGHTS]
        else:
            # 使用简单列表
            return self.NAMES

    def _get_weighted_names(self) -> List[Tuple[str, float]]:
        """
        获取带权重的名字列表。
        
        根据配置方式和分组设置，构建包含权重信息的名字列表，用于加权随机选择。
        
        Returns:
            List[Tuple[str, float]]: 名字和对应权重的元组列表，格式为 [(name1, weight1), (name2, weight2), ...]
            
        Raises:
            ValueError: 当指定的分组不存在时
            
        Note:
            - 对于 NAMES 配置，所有名字的权重默认为 1.0
            - 对于 NAMES_BY_GROUP 配置，使用 GROUP_WEIGHTS 中定义的组权重（默认为 1.0）
            - 对于 NAMES_WITH_WEIGHTS 配置，直接使用预定义的权重
        """
        if self.NAMES_WITH_WEIGHTS:
            if self.group:
                # 如果指定了分组，需要从 NAMES_BY_GROUP 中筛选对应的名字
                if self.NAMES_BY_GROUP and self.group in self.NAMES_BY_GROUP:
                    group_names = set(self.NAMES_BY_GROUP[self.group])
                    return [
                        (name, weight)
                        for name, weight in self.NAMES_WITH_WEIGHTS
                        if name in group_names
                    ]
                else:
                    # 如果没有分组信息，返回所有带权重的名字
                    return self.NAMES_WITH_WEIGHTS
            return self.NAMES_WITH_WEIGHTS
        elif self.NAMES_BY_GROUP:
            # 从分组数据构建带权重的名字列表
            weighted = []
            if self.group:
                # 如果指定了分组，只返回该分组的名字（使用该分组的权重）
                if self.group not in self.NAMES_BY_GROUP:
                    raise ValueError(
                        f"Group '{self.group}' not found in NAMES_BY_GROUP"
                    )
                group_weight = self.GROUP_WEIGHTS.get(self.group, 1.0)
                for name in self.NAMES_BY_GROUP[self.group]:
                    weighted.append((name, group_weight))
            else:
                # 如果没有指定分组，返回所有分组的名字（每个名字使用其所属分组的权重）
                for group, names in self.NAMES_BY_GROUP.items():
                    group_weight = self.GROUP_WEIGHTS.get(group, 1.0)
                    for name in names:
                        weighted.append((name, group_weight))
            return weighted
        else:
            # 使用简单列表，所有名字的权重相等（默认为 1.0）
            return [(name, 1.0) for name in self.NAMES]

    def generate(self, group: Optional[str] = None) -> str:
        """
        从列表中按权重随机选择一个名字。
        
        该方法支持分组和概率权重，可以在运行时临时指定分组。

        Args:
            group: 临时指定要使用的分组名称，会覆盖初始化时设置的分组
                  - None: 使用初始化时的分组设置
                  - str: 临时使用指定的分组

        Returns:
            str: 随机选择的名字
            
        Raises:
            ValueError: 当没有可用的名字时（例如分组为空）
            ValueError: 当指定的分组不存在时
        """
        # 临时使用指定的分组（保存原始分组以便恢复）
        original_group = self.group
        try:
            if group is not None:
                self.group = group

            weighted_names = self._get_weighted_names()
            if not weighted_names:
                raise ValueError("No names available for generation.")

            # 使用权重进行加权随机选择
            names, weights = zip(*weighted_names)
            return random.choices(names, weights=weights, k=1)[0]
        finally:
            # 恢复原始分组设置
            self.group = original_group

    def generate_many(
        self, count: int, allow_duplicates: bool = False, group: Optional[str] = None
    ) -> List[str]:
        """
        批量生成多个名字（支持去重和权重）。
        
        该方法提供了优化的批量生成实现，支持权重选择和去重控制。

        Args:
            count: 要生成的数量，必须为正整数
            allow_duplicates: 是否允许结果重复，默认为 False
                            - False: 确保所有结果不重复，如果可用数据不足会抛出异常
                            - True: 允许结果重复，使用加权随机选择
            group: 临时指定要使用的分组名称，会覆盖初始化时设置的分组
                  - None: 使用初始化时的分组设置
                  - str: 临时使用指定的分组

        Returns:
            List[str]: 生成的名字列表，默认不包含重复项

        Raises:
            ValueError: 当 count 小于等于 0 时
            ValueError: 当 allow_duplicates=False 且可用的不重复名字数量少于 count 时
            ValueError: 当指定的分组不存在时
            
        Note:
            - 当 allow_duplicates=False 时，结果数量受限于可用的不重复名字数量
            - 当 allow_duplicates=True 时，使用加权随机选择，可能会出现重复
            - 权重影响各个名字的出现概率，权重越大的名字被选中的概率越高
        """
        if count <= 0:
            raise ValueError(f"count must be positive, got {count}")

        # 临时使用指定的分组（保存原始分组以便恢复）
        original_group = self.group
        try:
            if group is not None:
                self.group = group

            available_names = self._get_available_names()
            unique_names = list(set(available_names))
            max_count = len(unique_names)

            if count > max_count and not allow_duplicates:
                raise ValueError(
                    f"Cannot generate {count} unique results. "
                    f"Only {max_count} unique names available. "
                    f"Set allow_duplicates=True to allow duplicates."
                )

            if count <= max_count:
                # 可用名字足够，使用权重进行不重复的随机选择
                weighted_names = self._get_weighted_names()
                if weighted_names:
                    # 去重并保留最大权重（同一名字可能在不同分组中有不同权重）
                    unique_weighted = {}
                    for name, weight in weighted_names:
                        if (
                            name not in unique_weighted
                            or weight > unique_weighted[name]
                        ):
                            unique_weighted[name] = weight
                    unique_weighted_list = list(unique_weighted.items())
                    unique_names_list, unique_weights = zip(*unique_weighted_list)

                    # 使用权重进行加权随机选择（不重复）
                    results = []
                    seen = set()
                    available_names = list(unique_names_list)
                    available_weights = list(unique_weights)

                    while len(results) < count and available_names:
                        # 按权重随机选择一个名字
                        selected = random.choices(
                            available_names, weights=available_weights, k=1
                        )[0]
                        results.append(selected)
                        seen.add(selected)

                        # 从可用列表中移除已选择的名字（确保不重复）
                        idx = available_names.index(selected)
                        available_names.pop(idx)
                        available_weights.pop(idx)

                    return results
                else:
                    # 无权重信息时，使用普通的随机采样
                    return random.sample(unique_names, count)
            else:
                # 可用名字不足但允许重复，使用权重生成（可能包含重复）
                weighted_names = self._get_weighted_names()
                if weighted_names:
                    names, weights = zip(*weighted_names)
                    return random.choices(list(names), weights=list(weights), k=count)
                else:
                    # 无权重信息时，从不重复的名字中随机重复选择
                    results = unique_names.copy()
                    while len(results) < count:
                        results.append(random.choice(unique_names))
                    random.shuffle(results)
                    return results
        finally:
            # 恢复原始分组设置
            self.group = original_group

    def get_groups(self) -> List[str]:
        """
        获取所有可用的分组名称。
        
        仅当子类使用 NAMES_BY_GROUP 配置时有效。

        Returns:
            List[str]: 分组名称列表，如果未使用分组配置则返回空列表
            
        Example:
            >>> water_margin = WaterMarginName()
            >>> groups = water_margin.get_groups()
            >>> print(groups)  # ['正派', '反派']
        """
        if self.NAMES_BY_GROUP:
            return list(self.NAMES_BY_GROUP.keys())
        return []
