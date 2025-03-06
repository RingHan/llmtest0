from openai import OpenAI # 导入OpenAI

client = OpenAI(base_url = "http://chatapi.littlewheat.com/v1",
                api_key  = "sk-QKqxOits92WRVsiQrkmyCfXy5n4hLQEZEZHF6IVbdNCgGS2r")

completion = client.chat.completions.create(
  model="gpt-4o-mini", # this field is currently unused
  messages=[
    {"role": "user",
    "content": "你好"}
  ],
  temperature=0.7,
)
print(completion.choices[0].message.content)# 输出文案