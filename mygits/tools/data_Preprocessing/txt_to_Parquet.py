import time
import json
import os
import re
import logging
from typing import List, Dict
from openai import OpenAI
import backoff
import pyarrow as pa
import pyarrow.parquet as pq

# noinspection SpellCheckingInspection
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 初始化 OpenAI 客户端
client = OpenAI(
    base_url="https://api.gptsapi.net/v1",
    api_key="sk-bPxb047a5bb6a60addce27af79928dc4be069203924Rfkrf"
)  # 替换为你的 API 密钥

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


@backoff.on_exception(backoff.expo, Exception, max_tries=5, factor=2)
def generate_single_entry(text: str) -> Dict:
    prompt = f"""
    参考以下文本，生成1个用于指令数据集的高质量条目。条目应该直接关联到给定的文本内容，选取一个问题类型并提出相关的问题。
    请确保生成多样化的指令类型，例如：
    -分析类问题参考："分析性奴学员目前的行为/心理是否达到合格性奴的标准？","分析校方此举有什么目的，对于调教性奴有什么效果？"
    -比较类问题参考："比较性奴学员目前的行为/心理相比学姐还有哪些不足，应该怎么改正？"
    -解释类问题参考："解释校方/教师/工作人员此命令或行为的目的？这种调教/训练方式有哪些优点？"
    -评价类问题参考："评价性奴学员目前的行为/心理是否符合校方的要求和期望"
    -问答类问题参考："为什么校方/教师/工作人员下达命令/进行这种行为？这种方式对于调教性奴有哪些优点？"

    文本内容：
    {text}

    output的回答需要完全从校方/教师/工作人员的角度进行回答，不要夹杂任何客观观点。请以下面的格式生成条目，确保所有字段都有内容：
    {{
        "instruction": "使用上述多样化的指令类型之一，提出一个具体的、与文本相关的问题或任务",
        "input": "如果需要额外的上下文信息，请在这里提供，否则留空",
        "output": "对instruction的详细回答或任务的完成结果"
    }}
    """

    try:
        response = client.chat.completions.create(
            model="claude-3-haiku-20240307",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,  # 增加温度以提高多样性
            max_tokens=4096
        )

        logger.info(f"API 响应: {response.choices[0].message.content}")

        # 使用正则表达式提取 JSON 数据
        json_match = re.search(r'\{.*\}', response.choices[0].message.content, re.DOTALL)
        if json_match:
            try:
                entry = json.loads(json_match.group())
                required_keys = ['instruction', 'input', 'output']
                if all(key in entry for key in required_keys):
                    # 设置 text 字段
                    if entry['input'].strip():
                        entry[
                            'text'] = (f"Below is an instruction that describes a task, paired with an input that "
                                       f"provides further context. Write a response that appropriately completes the "
                                       f"request.### Instruction: {entry['instruction']}\n### Input: "
                                       f"{entry['input']}\n### Response: {entry['output']}")
                    else:
                        entry[
                            'text'] = (f"Below is an instruction that describes a task. Write a response that "
                                       f"appropriately completes the request.### In"
                                       f"struction: {entry['instruction']}\n### Input: {entry['input']}\n### "
                                       f"Response: {entry['output']}")
                    logger.info("成功生成完整条目")
                    return entry
                else:
                    logger.warning("JSON 解析成功，但缺少必要字段")
                    return {"raw": json_match.group()}  # 仅保存原始数据片段
            except json.JSONDecodeError as e:
                logger.error(f"JSON 解析错误: {str(e)}")
                # 如果 JSON 解析失败，保存原始响应片段
                return {"raw": json_match.group()}  # 仅保存原始数据片段
        else:
            logger.error("无法从API响应中提取有效的JSON")
    except InternalServerError as e:
        logger.error(f"服务不可用: {str(e)}")
    except Exception as e:
        logger.error(f"生成条目时发生错误: {str(e)}")
        raise
    return {}


def generate_dataset(folder_path: str, entries_per_file: int = 2) -> List[Dict]:
    dataset = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            logger.info(f"正在处理文件: {filename}")
            text = read_file(file_path)
            for j in range(entries_per_file):
                logger.info(f"  生成第 {j + 1}/{entries_per_file} 个条目")
                entry = generate_single_entry(text)
                if entry:
                    dataset.append(entry)
                    logger.info(f"  成功生成 1 个条目")
                else:
                    logger.warning(f"  跳过不完整的条目")
    return dataset


def save_dataset_as_parquet(dataset: List[Dict], output_file: str):
    schema = pa.schema([
        ('instruction', pa.string()),
        ('input', pa.string()),
        ('output', pa.string()),
        ('text', pa.string()),
        ('raw', pa.string())
    ])

    arrays = [
        pa.array([entry.get('instruction', '') for entry in dataset]),
        pa.array([entry.get('input', '') for entry in dataset]),
        pa.array([entry.get('output', '') for entry in dataset]),
        pa.array([entry.get('text', '') for entry in dataset]),
        pa.array([entry.get('raw', '') for entry in dataset])
    ]

    table = pa.Table.from_arrays(arrays, schema=schema)
    pq.write_table(table, output_file)


def save_dataset_as_jsonl(dataset: List[Dict], output_file: str):
    with open(output_file, 'w', encoding='utf-8') as file:
        for entry in dataset:
            json.dump(entry, file, ensure_ascii=False)
            file.write('\n')


if __name__ == "__main__":
    input_folder = "D:/git/gitstorege/data/input/txt/pixiv/xingnuxunlianxueyuan"
    output_file_parquet = ("D:/git/gitstorege/data/output/Parquet/pixiv/xingnuxunlianxueyuan/xingnuxunlianxueyuan2"
                           ".parquet")
    output_file_jsonl = "D:/git/gitstorege/data/output/jsonl/pixiv/xingnuxunlianxueyuan/xingnuxunlianxueyuan2.jsonl"

    logger.info("开始生成数据集")
    dataset = generate_dataset(input_folder, entries_per_file=3)

    logger.info(f"保存数据集为 Parquet 格式到 {output_file_parquet}")
    save_dataset_as_parquet(dataset, output_file_parquet)

    logger.info(f"保存数据集为 JSONL 格式到 {output_file_jsonl}")
    save_dataset_as_jsonl(dataset, output_file_jsonl)

    logger.info(f"共生成 {len(dataset)} 个有效条目")
