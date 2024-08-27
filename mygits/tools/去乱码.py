#作者：Alex
#2024 / 8 / 25
#上午8: 33
import re


def remove_garbled_text_from_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式过滤非中文字符、英文、数字和常见标点符号，但保留换行符
    # 同时过滤掉所有可能的长度为3到8个字符的连续字母或数字组合
    cleaned_content = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9，。！？、：；“”‘’（）【】——\n]|[a-zA-Z0-9]{3,8}', '', content)

    # 将清理后的内容写回原文件，覆盖原内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)
        print(f"文件已成功保存到: {file_path}")


if __name__ == '__main__':
    file_path = r"D:\git\gitstorege\LLM_practice\ai\data\knowledge_base\txt\斗破苍穹同人\Chapter_7.txt"

    remove_garbled_text_from_file(file_path)