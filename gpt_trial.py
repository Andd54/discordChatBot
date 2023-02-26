import os
import openai
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv('API_KEY')  # API key

def checkLength(input):
    return (len(input) <= 500)


def response(promp):
    promp += " Please limit responses to 200 characters"
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
    conversation = "please select the funniest quote from this conversation: \n" + conversation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.5,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[";"]
    )
    result = "Funniest: "+response.choices[0].text
    return result


def bestOfWeek2(conversation):
    conversation = "please select the most raging quote from this conversation: \n" + conversation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.5,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[";"]
    )
    result = response.choices[0].text
    return "Most Raging: "+result


def bestOfWeek3(conversation):
    conversation = "please select the saddest quote from this conversation: \n" + conversation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.5,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[";"]
    )
    result = response.choices[0].text
    return "Saddest: "+result


def BOF(conversation):
    result = ''
    result += bestOfWeek(conversation) + '\n' + \
        bestOfWeek2(conversation) + '\n' + bestOfWeek3(conversation)
    return result


def summarize(conversation):
    conversation = 'Please summarize the following content: \n' + conversation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.5,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text

def simulate(user_messages):
    prompt = 'Below is a list of messages from a person. Please write a message in their exact style: \n'+user_messages
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text