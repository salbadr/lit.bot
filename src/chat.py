import os

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

load_dotenv()
persona = "You are a pirate"
developer_message = [
    {
        "role": "developer",
        "content": persona
    },

]

def chat_using_responses(client, message, prompt):
    try:
        message.append({
            "role": "user",
            "content": prompt
        })
        response = client.responses.create(
            model="gpt-5.4-nano",
            input=message,
            store=False,
            include=["reasoning.encrypted_content"],
        )

    except RateLimitError as e:
        print(f"There was a problem {e}")
    else:
        print(response.output_text)
        message += response.output


def chat_using_conversations(client, prompt, conversation_id, temperature):
    try:
        if conversation_id == '':
            conversation = client.conversations.create(items=developer_message)
            conversation_id = conversation.id

        message = [{
            "role": "user",
            "content": prompt
        }]

        response = client.responses.create(
            model="gpt-5.4-nano",
            input=message,
            conversation=conversation_id,
            temperature=float(temperature)
        )
    except RateLimitError as e:
        print(f"There was a problem {e}")
    else:
        print(response.output_text)
        return conversation_id


def main():
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    conversation_id = ''

    while True:

        prompt = input(
            "\nEnter nutritional advice that you seek or type END to end conversation:\n")

        if prompt.upper() != 'END':
            temperature = input("Enter temperature between 0 and 2: ")
            conversation_id = chat_using_conversations(
                client=client, prompt=prompt, conversation_id=conversation_id, temperature=temperature)
        else:
            break

    print("Thanks for using OpenAI chat")


if __name__ == "__main__":
    main()
