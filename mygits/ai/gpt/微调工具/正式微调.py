from openai import OpenAI
client = OpenAI(
    base_url="https://api.gptsapi.net/v1",
    api_key="sk-bPxb047a5bb6a60addce27af79928dc4be069203924Rfkrf"
)

client.files.create(
  file=open(r"D:\GPT\Jsonl\danmu.jsonl", "rb"),
  purpose="fine-tune"
)