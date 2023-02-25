import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('API_KEY')  # API key


def response(promp):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=promp,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[";"]
    )
    result = response.choices[0].text
    return result


def bestOfWeek(conversation):
    conversation = "please select the funniest quote of the week: \n" + conversation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[";"]
    )
    result = response.choices[0].text
    print(result)


podcast = open("./testcase.txt", "r").read()
bestOfWeek(podcast)
