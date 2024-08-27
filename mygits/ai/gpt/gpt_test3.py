from openai import OpenAI
client = OpenAI(
    base_url="https://api.gptsapi.net/v1",
    api_key="sk-bPxb047a5bb6a60addce27af79928dc4be069203924Rfkrf"
)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is a LLM?"}
  ]
)