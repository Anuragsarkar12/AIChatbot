from openai import OpenAI


api_key = 'your-api-key'
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "write an email to my boss for resignation?"
        },
        {
            "role": "user",
            "content": ""
        },
        {
            "role": "assistant"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
