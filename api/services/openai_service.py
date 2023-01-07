import os
import openai

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(message: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=100,
        temperature=0,
    )
    choices = response["choices"]
    response = choices[0]["text"]
    return response
