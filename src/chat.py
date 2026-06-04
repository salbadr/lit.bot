import os

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

load_dotenv()
persona = input("Enter persona for open ai chat below:\n")
prompt = input("Enter prompt for open ai chat below:\n")

try:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    response = client.responses.create(
        model="gpt-5.4-nano", 
        input=[
            {
                "role": "developer",
                "content": persona
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
except RateLimitError as e:
    print(f"There was a problem {e}")
else:
    print(response.output_text)
finally:
    print("Thanks for using OpenAI chat")
