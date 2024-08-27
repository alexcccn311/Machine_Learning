def detect_type(user_input):
    try:
        # 尝试将输入转换为整数
        value = int(user_input)
        return value, type(value)
    except ValueError:
        pass

    try:
        # 尝试将输入转换为浮点数
        value = float(user_input)
        return value, type(value)
    except ValueError:
        pass

    if user_input.lower() in ['true', 'false']:
        # 尝试将输入转换为布尔值
        value = user_input.lower() == 'true'
        return value, type(value)

    # 如果所有尝试都失败，返回原始字符串
    return user_input, type(user_input)

user_input = input('请输入你需要检测类型的内容：')
value, value_type = detect_type(user_input)
print(f'值: {value}, 类型: {value_type}')