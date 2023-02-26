import os, time, discord
from datetime import datetime, timedelta
from dotenv import load_dotenv
from gpt_trial import response, summarize, checkLength, simulate, BOF
from discord.ext import commands
import time


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='\\gpt-', intents=discord.Intents.all())

@bot.command(name="chat", help="Have a conversation with GPT-3!")
async def gpt(ctx, *, arg):
    if (checkLength(arg)):
        await ctx.send(response(arg))
    else:
        ctx.send("Please Keep Prompts under 500 char")

@bot.command(name="summarize", help="Summarize last conversation, number n is last n minutes summarized")
async def summate(ctx,n=None):
    if (n == None):
        await ctx.send("Invalid Format: For \\gpt-summarize, Please include 1 number indicating the last n minutes to be summarized")
        return
    try: 
        n = int(n)
    except ValueError:
        await ctx.send("Invalid Format: For \\gpt-summarize, Please include 1 number indicating the last n minutes to be summarized")
        return
    all_messages = ""
    async for message in ctx.channel.history(limit=200):
        if (str(message.content).__contains__("\\gpt") or message.author == bot.user):
            continue
        if checkLength(str(message.content)) and (time.time() - message.created_at.timestamp()) < (n * 60) :
            all_messages += str(message.author.name) + ":"
            all_messages += message.content + ","
            last = message.created_at.timestamp()
        else:
            break
    await ctx.send(summarize(all_messages))

@bot.command(name="best", help="Select the best quote from the past n days!")
async def best(ctx, n=None):
    if (n == None):
        await ctx.send("Invalid Format: For \\gpt-best, Please include 1 number indicating the last n days to choose from")
        return
    try: 
        n = int(n)
    except ValueError:
        await ctx.send("Invalid Format: For \\gpt-best, Please include 1 number indicating the last n days to choose from")
        return
    messages = ""
    async for message in ctx.channel.history(limit=10000, after=datetime.today() - timedelta(days=int(n))):
        if message.author != bot.user and checkLength(str(message.content)) and not(str(message.content).__contains__("\\gpt")):
            messages += str(message.author) + ": '" + message.content + "'\n"
    print(messages)
    await ctx.send(BOF(messages))

@bot.command(name="sim", help="Simulate a user's messages!")
async def sim(ctx, user=None):
    if (user == None):
        await ctx.send("Invalid Format: For \\gpt-summarize, Please include a user to simulate (using @ notation)")
        return
    messages = ""
    track = False
    async for message in ctx.channel.history(limit=10000):
        if message.author.mention == user and checkLength(str(message.content)):
            track = True
            messages = message.content + '\n' + messages
    print(messages)
    if (track):
        await ctx.send(simulate(messages))
    else:
        await ctx.send("No User Messages found. Hint: Make sure you are using @ notation")

bot.run(TOKEN)