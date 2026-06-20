import os
import asyncio

from dotenv import load_dotenv
from openai import AsyncOpenAI, RateLimitError

load_dotenv()
persona = "You are an english teacher whose purpose is to help students from grade 4 to grade 8" \
    "in the Ontario region of Canada with improving reading and comprehension skills." \
    "The conversation will start off with the student/user providing the genre that they will like to read from " \
    "As such, you are to provide them with a small passage, consisting of 3 paragraphs, to read and then ask them one multiple choice question about the passage. "\
    "After the student responds then you will ask another multiple choice question until the interaction ends." \
    "You will then provide feedback on their answers and suggest ways to improve their reading and comprehension skills."

developer_message = [
    {
        "role": "developer",
        "content": persona
    },

]

# Not used but kept for reference


async def chat_using_responses(client, message, prompt):
    try:
        message.append({
            "role": "user",
            "content": prompt
        })
        response = await client.responses.create(
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


async def chat_using_conversations(client, prompt, conversation_id):
    try:
        if conversation_id == '':
            conversation = await client.conversations.create(items=developer_message)
            conversation_id = conversation.id

        message = [{
            "role": "user",
            "content": prompt
        }]

        response = await client.responses.create(
            model="gpt-5.4-nano",
            input=message,
            conversation=conversation_id,
        )
    except RateLimitError as e:
        print(f"There was a problem {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        return {
            "output_text": response.output_text,
            "conversation_id": conversation_id,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "total_tokens": response.usage.total_tokens
            }
        }


def print_statistics(usage):
    input_tokens, output_tokens, total_tokens = usage[
        "input_tokens"], usage["output_tokens"],  usage['total_tokens']

    max_tokens = 1_000_000   # 1 million tokens
    input_price = 0.20  # input token costs
    output_price = 1.25  # output token costs

    cost_incurred = (input_tokens * input_price +
                     output_tokens * output_price) / max_tokens

    print("\nUSAGE STATISTICS")
    print(f"The input token count is {input_tokens}")
    print(f"The output token count is {output_tokens}")
    print(f"The total token count is {total_tokens}")

    print(f"Rough cost estimate is ${cost_incurred:.6f}")


async def main():
    client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    conversation_id = ''

    prompt = input(
        "\nEnter the genre that you will like to read. Type END to end conversation:\n")
    while prompt.upper() != 'END':

        response = await chat_using_conversations(
            client=client, prompt=prompt, conversation_id=conversation_id)

        conversation_id = response.get('conversation_id')
        output_text = response.get('output_text')
        usage = response.get('usage')
        print(f"\n{output_text}")
        print_statistics(usage=usage)

        prompt = input("\nEnter response or type END to end conversation:\n")
    print("Thanks for using OpenAI chat")


if __name__ == "__main__":
    asyncio.run(main())
