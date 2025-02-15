class LoraBlockWeight_Flux:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "layer_or_multi_layer": ("STRING", {
                    "multiline": False,  # True if you want the field to look like the one on the ClipTextEncode node
                    "default": "15表示15层权重为0，2-10表示2-10层权重为0",
                    "lazy": True
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("block_vector",)
    FUNCTION = "test"

    CATEGORY = "Snap Processing"

    def modify_numbers(self, indices_to_zero):
        # 创建一个包含58个1的列表
        numbers = [1] * 58

        # 解析范围表示法（例如 '2-10'）
        indices = []
        # 确保传入的是一个列表
        if isinstance(indices_to_zero, str):
            indices_to_zero = [indices_to_zero]

        for item in indices_to_zero:
            item = str(item)  # 确保 item 是字符串类型

            if '-' in item:  # 处理范围
                try:
                    start, end = map(int, item.split('-'))
                    indices.extend(range(start, end + 1))  # 从1开始的索引，直接使用范围
                except ValueError:
                    continue  # 如果范围无效，忽略该部分
            else:  # 处理单个索引
                try:
                    indices.append(int(item))  # 直接使用用户输入的值
                except ValueError:
                    continue  # 如果不是有效数字，忽略该部分

        # 根据传入的索引列表，将对应位置的数字改为0
        for index in indices:
            if 0 <= index < len(numbers):
                numbers[index - 1] = 0  # 使用直接映射的索引，减1来设置对应位置为0

        return numbers

    def test(self, layer_or_multi_layer):
        # 解析输入的layer_or_multi_layer，支持单个数字、多个数字、范围
        indices = []
        # 将用户输入的字符串按逗号分割，处理每一部分
        for item in layer_or_multi_layer.split(","):
            item = item.strip()  # 去除前后空格
            if '-' in item:  # 处理范围
                try:
                    start, end = map(int, item.split('-'))
                    indices.extend(range(start, end + 1))  # 生成范围内的索引并加入列表（从1到5，索引为1到5）
                except ValueError:
                    continue  # 如果范围无效，忽略该部分
            else:  # 处理单个索引
                try:
                    indices.append(int(item))  # 使用用户输入的值
                except ValueError:
                    continue  # 如果不是有效数字，忽略该部分

        # 调用 modify_numbers 方法，处理索引
        modified_numbers = self.modify_numbers(indices)

        # 将修改后的数字列表转为字符串，逗号分隔
        modified_strings = ','.join(map(str, modified_numbers))  # 将数字转换为字符串并用逗号连接

        return (modified_strings,)


# 节点类映射，确保节点名称唯一
NODE_CLASS_MAPPINGS = {
    "LoraBlockWeight_Flux": LoraBlockWeight_Flux
}

# 人类可读的节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "LoraBlockWeight_Flux": "LoraBlockWeight_Flux"
}
