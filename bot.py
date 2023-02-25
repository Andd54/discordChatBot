import os
import discord
from dotenv import load_dotenv

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
    print(str(message.content))
    if message.author == client.user:
        return

    if message.content:
        await message.channel.send('Hello!')

async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
client.run(TOKEN)