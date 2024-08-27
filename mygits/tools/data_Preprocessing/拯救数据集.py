import re
import json

# 文件路径
input_file_path = 'D:/git/gitstorege/data/output/Parquet/pixiv/xingnuxunlianxueyuan/data.txt'  # 替换为你的输入文件路径
output_file_path = 'D:/git/gitstorege/data/output/json/pixiv/xingnuxunlianxueyuan/xingnuxunlianxueyuan.jsonl'  # 替换为你希望保存的输出文件路径

# 读取并处理输入文件
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# 使用正则表达式提取所有 {} 之间的内容
json_objects = re.findall(r'\{.*?\}', data, re.DOTALL)

# 保存提取的 JSON 数据到 JSONL 文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for json_object in json_objects:
        output_file.write(json_object + '\n')

print(f"提取后的数据已保存到 {output_file_path}")