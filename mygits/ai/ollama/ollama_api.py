import ollama
import json
import os


def load_history(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []


def save_history(file_path, context):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(context, file, ensure_ascii=False, indent=4)


def load_knowledge_base(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    return ""


def chat_with_ollama():
    context_file = 'chat_history.json'
    knowledge_base_file = 'knowledge_base.txt'

    context = load_history(context_file)
    knowledge_base = load_knowledge_base(knowledge_base_file)

    if knowledge_base:
        context.append({'role': 'system', 'content': knowledge_base})

    model_name = 'Llama3-8b-chinese-Uncensored:latest'

    while True:
        user_input = input("你: ")
        if user_input.lower() in ["退出", "exit"]:
            print("聊天结束。")
            break

        context.append({'role': 'user', 'content': user_input})

        stream = ollama.chat(
            model=model_name,
            messages=context,
            stream=True,
        )

        response = ''
        for chunk in stream:
            response += chunk['message']['content']

        print(f"AI: {response}")
        context.append({'role': 'assistant', 'content': response})

        save_history(context_file, context)


if __name__ == "__main__":
    chat_with_ollama()