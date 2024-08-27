import json
import os

def convert_txt_to_jsonl(txt_folder, jsonl_file):
    # 打开输出文件
    with open(jsonl_file, 'w', encoding='utf-8') as outfile:
        # 遍历txt文件夹中的所有txt文件
        for txt_file in os.listdir(txt_folder):
            if txt_file.endswith('.txt'):
                # 构建txt文件的完整路径
                txt_path = os.path.join(txt_folder, txt_file)
                # 读取txt文件内容
                with open(txt_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    # 创建JSON对象
                    json_object = {
                        "title": os.path.splitext(txt_file)[0],  # 文件名作为标题
                        "content": content
                    }
                    # 将JSON对象写入JSONL文件
                    outfile.write(json.dumps(json_object, ensure_ascii=False) + '\n')

# 定义txt文件夹路径和输出的jsonl文件路径
txt_folder = r'D:\GPT\TXT'
jsonl_file = r'D:\GPT\Jsonl\danmu.jsonl'

# 执行转换
convert_txt_to_jsonl(txt_folder, jsonl_file)