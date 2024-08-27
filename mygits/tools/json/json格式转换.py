import json

# 读取原始 JSON 数据
with open(r"D:\git\gitstorege\json\GPT\danmu.json", 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]

# 准备存储转换后的数据
converted_data = []

# 处理每一行数据
for item in data:
    messages = item['messages']
    instruction = messages[0]['content']
    user_input = messages[1]['content']
    output = messages[2]['content']

    # 构建新的 JSON 格式
    new_format = {
        "instruction": instruction,
        "input": user_input,
        "output": output
    }

    converted_data.append(new_format)

# 将转换后的数据写入新的 JSON 文件，每个对象占据多行
with open(r"D:\git\gitstorege\json\llama3\danmu.json", 'w', encoding='utf-8') as f:
    for item in converted_data:
        f.write(json.dumps(item, ensure_ascii=False, indent=2) + '\n')