import os, time, discord
from datetime import datetime, timedelta
from dotenv import load_dotenv
from gpt_trial import response, BOF, simulate
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='\\gpt-', intents=discord.Intents.all())

@bot.command(name="chat", help="Have a conversation with GPT-3!")
async def gpt(ctx, *, arg):
    await ctx.send(response(arg))

@bot.command(name="best", help="Select the best quote from the past n days!")
async def best(ctx, n):
    messages = ""
    async for message in ctx.channel.history(limit=10000, after=datetime.today() - timedelta(days=int(n))):
        if message.author != bot.user:
            messages += str(message.author) + ": '" + message.content + "'\n"
    print(messages)
    await ctx.send(BOF(messages))

@bot.command(name="sim", help="Simulate a user's messages!")
async def sim(ctx, user):
    messages = ""
    async for message in ctx.channel.history(limit=10000):
        if message.author.mention == user:
            messages = message.content + '\n' + messages
    print(messages)
    await ctx.send(simulate(messages))

bot.run(TOKEN)