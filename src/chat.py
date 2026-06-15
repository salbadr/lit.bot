import os

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

load_dotenv()
persona = "You are a pirate"


def chat_using_responses(client, input_history, prompt):
    try:
        input_history.append({
            "role": "user",
            "content": prompt
        })
        response = client.responses.create(
            model="gpt-5.4-nano",
            input=input_history,
            store=False,
            include=["reasoning.encrypted_content"],
        )

    except RateLimitError as e:
        print(f"There was a problem {e}")
    else:
        print(response.output_text)
        input_history += response.output


def chat_using_conversations(client, prompt, conversation_id):
    try:
        if conversation_id == '':
            conversation = client.conversations.create(items=[
                {
                    "role": "developer",
                    "content": persona
                },
            ])
            conversation_id = conversation.id

        messages = [{
            "role": "user",
            "content": prompt
        }]

        response = client.responses.create(
            model="gpt-5.4-nano",
            input=messages,
            conversation=conversation_id
        )
    except RateLimitError as e:
        print(f"There was a problem {e}")
    else:
        print(response.output_text)
        return conversation_id


def main():
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    input_history = [
        {
            "role": "developer",
            "content": persona
        },

    ]
    conversation_id = ''
    while True:

        prompt = input(
            "\nEnter nutritional advice that you seek or type END to end conversation:\n")

        if prompt.upper() != 'END':
            conversation_id = chat_using_conversations(
                client=client, prompt=prompt, conversation_id=conversation_id)
        else:
            break

    print("Thanks for using OpenAI chat")


if __name__ == "__main__":
    main()
