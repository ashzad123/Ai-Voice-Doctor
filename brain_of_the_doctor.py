from dotenv import load_dotenv
import os
from groq import Groq
import base64

load_dotenv()

# Step1: Setup GROQ API key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Step2: Convert image to required format


def encode_image(image_path):
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode("utf-8")


# Step3: Setup Multimodal LLM

query = "Is there something wrong with my face?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"


def analyze_image_with_query(query, model, encoded_image):
    client = Groq()
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

    return chat_completion.choices[0].message.content
