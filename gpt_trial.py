import os
import openai

openai.api_key = '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'  # API key

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
    print(result)
    return

def bestOfWeek(conversation):
    

response("what day is it today?")
