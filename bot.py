import os, time, discord
from dotenv import load_dotenv
from gpt_trial import response
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='\\gpt-', intents=discord.Intents.all())

@bot.command(name="chat", help="Have a conversation with GPT-3!")
async def gpt(ctx, *, arg):
    await ctx.send(response(arg))

bot.run(TOKEN)