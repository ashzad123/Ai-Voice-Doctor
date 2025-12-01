from dotenv import load_dotenv

load_dotenv()
from groq import Groq

import os
import base64

image = "acne.jpg"
image_file = open(image, "rb")
encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

client = Groq()
model = "meta-llama/llama-4-scout-17b-16e-instruct"
query = "Is there something wrong with my face?"

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": query},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}",
                },
            },
        ],
    }
]

chat_completion = client.chat.completions.create(messages=messages, model=model)

print(chat_completion.choices[0].message.content)
