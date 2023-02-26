# discordChatBot
HackIllinois 2023
Developed by Neil, Sean, Ziyi
Using GPT 3.0 and extend its functionality by the combination as a discord chatbot

Have Fun

## Setup
To use this bot, you must first make your own version of it.
Why? OpenAI allows a single user a limited amount of credits. In order to ensure that this limit isn't hit, every user must have their own account.

## 1. Initial setup
Clone the Repository
Run 
```
pip install -r requirements.txt
```

## 2. Create a discord bot
Go to https://discord.com/developers/applications 

Create an application (doesn't matter what it is named)

Create a bot via the bots tab on the left hand side

Name the bot whatever you desire and set its icon (optional)

Enable ALL status switches on the right side EXCEPT REQUIRES OAUTH2 CODE GRANT

Save your permissions

Copy token (you may have to reset it first)

Open the .env file from the repository and paste your token after DISCORD_TOKEN = 

Go back to the webpage and open OAuth2 on the left hand side

Click on 'URL Generator'

Select 'Bot' for scope and 'Admin' for permissions (If you are worried about what the bot might do, feel free to look at the code and ensure its safety)

Copy the generated URL and give it permission in your server(s)


## 3. Get your openAI account key
Go to https://platform.openai.com/account/api-keys

Sign in or create an account

Press 'create new secret key' and copy it

Paste the key into the .env file of your repository after API_KEY =

*Note: I reccomend you also save these keys in .env.save, in case you need to pull again and lose your keys

## 4 Running the bot
Open a terminal or command prompt

Navigate to your directory

Run
```
python bot.py
```
