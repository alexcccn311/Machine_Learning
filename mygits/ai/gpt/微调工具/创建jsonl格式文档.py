import json

# 创建一些示例数据
data = [
    {},]

# 定义输出文件路径
jsonl_file = r'D:\GPT\Jsonl'

# 打开输出文件，写入数据
with open(jsonl_file, 'w', encoding='utf-8') as outfile:
    for entry in data:
        json.dump(entry, outfile, ensure_ascii=False)
        outfile.write('\n')