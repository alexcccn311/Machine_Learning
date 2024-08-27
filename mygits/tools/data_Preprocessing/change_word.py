import os  # 导入os模块，用于与操作系统进行交互


def replace_text_from_jsonl_files(directory, original_format, target_text, new_text):
    """
    在指定的目录中遍历所有.jsonl文件，并将其中的目标文本替换为新文本。

    :param directory: str, 要处理的文件夹的绝对路径
    :param target_text: str, 需要查找并替换的目标文本
    :param new_text: str, 替换目标文本的新文本
    """
    # 检查给定的目录是否存在
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")  # 如果目录不存在，打印错误信息并返回
        return  # 提前结束函数

    # 遍历给定目录及其子目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 只处理以.jsonl结尾的文件
            if file.endswith(f".{original_format}"):
                file_path = os.path.join(root, file)  # 获取文件的完整路径

                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()  # 将文件内容读取为一个字符串

                # 检查文件中是否包含目标文本
                if target_text in content:
                    print(f"在 {file_path}找到 '{target_text}'")  # 如果找到目标文本，打印相关信息
                else:
                    print(f"没有在{file_path}中找到'{target_text}'")  # 如果没有找到目标文本，打印相关信息
                    continue  # 跳过此文件，继续下一个文件的处理

                # 替换目标文本为新文本
                modified_content = content.replace(target_text, new_text)

                # 将修改后的内容写回到文件中，覆盖原文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)  # 写入修改后的内容
                print(f"修改完成: {file_path}")  # 打印修改完成的提示信息


if __name__ == '__main__':
    # 调用函数，传入要处理的目录路径，目标文本和新文本
    replace_text_from_jsonl_files(r"D:\git\gitstorege\LLM_practice\ai\data\knowledge_base\txt\性奴训练学院",   # 目标目录路径txt,'"')
