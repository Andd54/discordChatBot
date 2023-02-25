import os
import discord
from dotenv import load_dotenv
from gpt_trial import response
import time

BUFFER = 10
current_time = time.time()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

print(TOKEN)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}'
    )

@client.event
async def on_message(message):
    global current_time
    if time.time() - current_time > BUFFER:
        if message.author == client.user:
            return

        if message.content:
            await message.channel.send(response(message.content))

client.run(TOKEN)