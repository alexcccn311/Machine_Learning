import json
from collections import defaultdict

# 使用原始字符串避免转义字符问题
file_path = r"D:\GPT\Jsonl\danmu.jsonl"

# 读取文档数据
dataset = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        dataset.append(json.loads(line.strip()))

# 初始化一个用于统计格式错误的字典，值的类型为int，默认值为0
format_errors = defaultdict(int)

# 遍历数据集中每个示例
for ex in dataset:
    # 检查示例是否为字典类型，如果不是则计数并跳过该示例
    if not isinstance(ex, dict):
        format_errors["data_type"] += 1
        continue

    # 获取示例中的messages字段，如果不存在则计数并跳过该示例
    messages = ex.get("messages", None)
    if not messages:
        format_errors["missing_messages_list"] += 1
        continue

    # 遍历messages列表中的每条消息
    for message in messages:
        # 检查消息中是否存在"role"和"content"字段，如果缺失则计数
        if "role" not in message or "content" not in message:
            format_errors["message_missing_key"] += 1

        # 检查消息中是否存在未识别的键，如果有则计数
        if any(k not in ("role", "content", "name", "function_call", "weight") for k in message):
            format_errors["message_unrecognized_key"] += 1

        # 检查消息中的"role"字段是否为预定义的值之一，如果不是则计数
        if message.get("role", None) not in ("system", "user", "assistant", "function"):
            format_errors["unrecognized_role"] += 1

        # 获取消息中的"content"和"function_call"字段
        content = message.get("content", None)
        function_call = message.get("function_call", None)

        # 检查消息中是否缺少"content"字段或其值是否为空字符串，如果是则计数
        if (not content and not function_call) or not isinstance(content, str):
            format_errors["missing_content"] += 1

    # 检查messages列表中是否存在"role"为"assistant"的消息，如果不存在则计数
    if not any(message.get("role", None) == "assistant" for message in messages):
        format_errors["example_missing_assistant_message"] += 1

# 如果存在格式错误，则打印错误类型及其数量，否则打印未发现错误
if format_errors:
    print("Found errors:")
    for k, v in format_errors.items():
        print(f"{k}: {v}")
else:
    print("No errors found")