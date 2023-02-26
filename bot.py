import os, time, discord
from datetime import datetime, timedelta
from dotenv import load_dotenv
from gpt_trial import response, BOF
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

bot.run(TOKEN)