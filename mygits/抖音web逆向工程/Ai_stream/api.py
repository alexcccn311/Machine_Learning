from openai import OpenAI


def initialize_client(api_dict, api_name):
    # 获取 API 配置
    config = api_dict.get(api_name)
    if config:
        base_url = config['base_url']
        api_key = config['api_key']
    else:
        raise ValueError(f"Port name {api_name} not found in api_dict")

    # 初始化 OpenAI 客户端
    client = OpenAI(
        base_url=base_url,
        api_key=api_key
    )

    return client