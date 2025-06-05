from together import Together
from dotenv import load_dotenv
import os

load_dotenv()
api_key =os.getenv("TOGETHER_API_KEY")
client = Together(api_key=api_key) # auth defaults to os.environ.get("TOGETHER_API_KEY")

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
      {
        "role": "user",
        "content": "Who is Hazrat Muhammad PBUH?"
      }
    ]
)
print(response.choices[0].message.content)