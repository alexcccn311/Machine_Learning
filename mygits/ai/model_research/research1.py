from safetensors import safe_open

# 替换为你的 .safetensors 文件路径
file_path = r"D:\git\gitstorege\original_model\Llama3.1-8B-Chinese-Chat\model-00001-of-00004.safetensors"

with safe_open(file_path, framework="pt") as f:
    for key in f.keys():
        tensor = f.get_tensor(key)
        print(f"Parameter: {key}, Values: {tensor}")