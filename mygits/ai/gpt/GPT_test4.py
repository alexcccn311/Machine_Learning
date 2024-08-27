import os
import openai
from openai import OpenAI
client = OpenAI(
    base_url="https://api.gptsapi.net/v1",
    api_key="sk-bPxb047a5bb6a60addce27af79928dc4be069203924Rfkrf"
)

knowledge_base = """
我们直播间售卖的产品为泰国旅行产品，两大一小三人同行的价格为2499.行程包括曼谷，芭提雅和星梦岛。
"""

def chat_with_gpt(user_input):
    # 将知识库添加到提示的一部分
    prompt = knowledge_base + "\n\n用户: " + user_input + "\n客服: "
    response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {"role": "assistant", "content": "You are a sales."},
        {"role": "user", "content": user_input},
    ],
    temperature=0.8,
    max_tokens=256,
    top_p=1
    )
    print(response.choices[0].message.content)
chat_with_gpt(input())