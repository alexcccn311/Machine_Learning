import json


def clean_raw_entry(raw_entry: str) -> dict:
    # 移除多余的换行符和反斜杠
    cleaned_raw = raw_entry.replace("\\n", "").replace("\\", "")

    # 尝试解析嵌套的 JSON 数据
    nested_entry = json.loads(cleaned_raw)
    return {
        "instruction": nested_entry.get("instruction", ""),
        "input": nested_entry.get("input", ""),
        "output": nested_entry.get("output", "")
    }


def clean_jsonl_data(input_file: str, output_file: str):
    cleaned_data = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            # 解析外层 JSON 数据
            entry = json.loads(line)

            # 检查是否有 "raw" 字段
            if "raw" in entry:
                # 解析内层 JSON 数据并清理
                cleaned_entry = clean_raw_entry(entry.get("raw", ""))
            else:
                # 保留核心字段，移除不需要的字段
                cleaned_entry = {
                    "instruction": entry.get("instruction", ""),
                    "input": entry.get("input", ""),
                    "output": entry.get("output", "")
                }

            # 添加清理后的条目
            if cleaned_entry.get("instruction") or cleaned_entry.get("input") or cleaned_entry.get("output"):
                cleaned_data.append(cleaned_entry)

    # 将清洗后的数据保存为新的 JSONL 文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in cleaned_data:
            json.dump(entry, outfile, ensure_ascii=False)
            outfile.write('\n')


if __name__ == "__main__":
    input_file = "D:/git/gitstorege/data/output/jsonl/pixiv/xingnuxunlianxueyuan/xingnuxunlianxueyuan2.jsonl"  # 替换为你的输入文件路径
    output_file = "D:/git/gitstorege/data/output/jsonl/pixiv/xingnuxunlianxueyuan/xingnuxunlianxueyuan3.jsonl"  # 替换为你想要保存的输出文件路径

    clean_jsonl_data(input_file, output_file)
    print(f"清洗后的数据已保存到 {output_file}")