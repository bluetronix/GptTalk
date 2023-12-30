import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key='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',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is computer programming?",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)