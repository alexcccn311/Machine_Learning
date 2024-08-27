from opencc import OpenCC

def convert_traditional_to_simplified(file_path, output_path):
    cc = OpenCC('t2s')  # 创建转换器
    with open(file_path, 'r', encoding='utf-8') as file:
        traditional_text = file.read()
    simplified_text = cc.convert(traditional_text)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(simplified_text)
    print("转换完成并保存到:", output_path)

# 调用函数，传入繁体中文文件路径和简体中文输出文件路径
convert_traditional_to_simplified('D:/git/gitstorege/LLM_practice/ai/data/knowledge_base/txt/如何训练厕奴.txt',
                                  'D:/git/gitstorege/LLM_practice/ai/data/knowledge_base/txt/如何训练厕奴简体.txt')