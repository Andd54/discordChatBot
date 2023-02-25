import os
import openai
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv('API_KEY')  # API key


def response(promp):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=promp,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
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
    return result


def bestOfWeek2(conversation):
    conversation = "please select the most raging quote of the week: \n" + conversation
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
    return result


def bestOfWeek3(conversation):
    conversation = "please select the saddest quote of the week: \n" + conversation
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
    return result


def BOF(conversation):
    result = ''
    result += bestOfWeek(conversation) + '\n' + \
        bestOfWeek2(conversation) + '\n' + bestOfWeek3(conversation)
    return result


def summarize(conversation):
    conversation = 'Please summarize the content: \n' + conversation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text
