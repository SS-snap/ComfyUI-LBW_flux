def modify_numbers(indices_to_zero):
    # 创建一个包含58个1的列表
    numbers = [1] * 58

    # 解析范围表示法（例如 '2-10'）
    indices = []
    for item in indices_to_zero:
        if '-' in item:  # 处理范围
            start, end = map(int, item.split('-'))
            indices.extend(range(start, end + 1))  # 生成范围内的索引并加入列表
        else:  # 处理单个索引
            indices.append(int(item))

    # 根据传入的索引列表，将对应位置的数字改为0
    for index in indices:
        if 0 <= index < len(numbers):
            numbers[index] = 0

    return numbers


# 示例使用：将索引为2到10的数字改为0，以及索引为15的数字改为0
indices = ["2-10", "15"]
modified_numbers = modify_numbers(indices)

print(modified_numbers)
