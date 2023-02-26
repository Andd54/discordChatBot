import os, time, discord
from datetime import datetime, timedelta
from dotenv import load_dotenv
from gpt_trial import response, summarize, checkLength, simulate, BOF
from discord.ext import commands
import time


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
conversation = ""
started = False
channel = None

bot = commands.Bot(command_prefix='\\gpt-', intents=discord.Intents.all())



@bot.command(name="chat", help="Have a conversation with GPT-3")
async def gpt(ctx, arg = commands.parameter(default=None, description="input for GPT-3")):
    if (arg == None):
        await ctx.send("Invalid Format: For \\gpt-chat, Please include a prompt")
        return
    
    if (checkLength(arg)):
        await ctx.send(response(arg))
    else:
        ctx.send("Please Keep Prompts under 500 char")

@bot.command(name="summarize", help="Summarize the last n minutes of a conversation")
async def summate(ctx,n = commands.parameter(default=None, description="number of minutes to summarize"),channel = commands.parameter(default=None, description="channel to summarize")):
    if (n == None):
        await ctx.send("Invalid Format: For \\gpt-summarize, Please include 1 number indicating the last n minutes to be summarized")
        return
    try: 
        n = int(n)
    except ValueError:
        await ctx.send("Invalid Format: For \\gpt-summarize, Please include 1 number indicating the last n minutes to be summarized")
        return
    
    if channel == None:
        channel = ctx.channel
    else:
        channel = bot.get_channel(int(channel[2:-1]))

    all_messages = ""
    async for message in channel.history(limit=100):
        if (str(message.content).__contains__("\\gpt") or message.author == bot.user):
            continue
        if checkLength(str(message.content)) and (time.time() - message.created_at.timestamp()) < (n * 60) :
            all_messages += str(message.author.name) + ":"
            all_messages += message.content + ","
            last = message.created_at.timestamp()
        else:
            break
    await ctx.send(summarize(all_messages))

@bot.command(name="best", help="Select the best quote from the past n days in the current or specified channel")
async def best(ctx, n = commands.parameter(default=None, description="number of days to choose from"), channel = commands.parameter(default=None, description="channel to choose from")):
    if (n == None):
        await ctx.send("Invalid Format: For \\gpt-best, Please include 1 number indicating the last n days to choose from")
        return
    try: 
        n = int(n)
    except ValueError:
        await ctx.send("Invalid Format: For \\gpt-best, Please include 1 number indicating the last n days to choose from")
        return
    
    if channel == None:
        channel = ctx.channel
    else:
        channel = bot.get_channel(int(channel[2:-1]))

    messages = ""
    async for message in channel.history(limit=100, after=datetime.today() - timedelta(days=int(n))):
        if message.author != bot.user and checkLength(str(message.content)) and not(str(message.content).__contains__("\\gpt")):
            messages += str(message.author) + ": '" + message.content + "'\n"
    await ctx.send(BOF(messages))

@bot.command(name="sim", help="Simulate a user's messages in the current or specified channel")
async def sim(ctx, user = commands.parameter(default=None, description="User to simulate"), channel = commands.parameter(default=None, description="Channel to gather data from"), minimum_characters = commands.parameter(default=None, description="Minimum character count for messages to be considered")):
    if (user == None):
        await ctx.send("Invalid Format: For \\gpt-sim, Please include a user to simulate (using @ notation)")
        return
    
    if (minimum_characters == None):
        minimum_characters = 0
    else:
        try: 
            minimum_characters = int(minimum_characters)
        except ValueError:
            await ctx.send("Invalid Format: For \\gpt-sim, Please include a valid minimum character count")
            return
    
    if channel == None:
        channel = ctx.channel
    else:
        try:
            channel = bot.get_channel(int(channel[2:-1]))
        except ValueError:
            await ctx.send("Invalid Format: For \\gpt-sim, Please include a valid channel (using # notation)")
            return

    if channel == None:
        await ctx.send("Invalid Format: For \\gpt-sim, Please include a valid channel (using # notation)")
        return

    messages = ""
    track = False
    async for message in channel.history(limit=100):
        if message.author.mention == user and checkLength(str(message.content)) and len(message.content) > minimum_characters:
            track = True
            messages = message.content + '\n' + messages
    
    if (track):
        await ctx.send(simulate(messages))
    else:
        await ctx.send("No User Messages found. Hint: Make sure you are using @ notation")

@bot.command(name="start", help="Start a conversation with GPT-3")
async def start(ctx, *args):
    global channel, conversation
    conversation = "Previously, we had the following conversation, please continue it: \n"
    channel = ctx.channel
    await ctx.send(response("Hello!"))

@bot.command(name="stop", help="Stop a conversation with GPT-3")
async def stop(ctx, *args):
    global channel, conversation
    channel = None
    conversation = ""
    await ctx.send(response("Goodbye!"))

@bot.event
async def on_message(message):
    if (message.author == bot.user):
        return
    if (message.channel == channel and message.content != "\\gpt-start" and message.content != "\\gpt-stop"):
        global conversation
        conversation += message.author.name + ": " + message.content + "\n"
        responding = response(conversation)
        if responding:
            conversation += "GPT-3: " + responding + "\n"
            await message.channel.send(responding)
    await bot.process_commands(message)

bot.run(TOKEN)