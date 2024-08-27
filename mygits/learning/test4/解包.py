def detect_type(user_input): #def定义的对象为函数，函数可以包含用户输入，随机数等不确定值，函数可以包含return返回值也可以不包含，可以return一个数据，也可以return多个数据，函数本身就是最常见的对象可供其他代码调用和解包。
    try:
        # 尝试将输入转换为整数
        value = int(user_input)
        return value, type(value) # 如果成功，这里会立即返回，后续代码不会执行.return自带中止命令
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