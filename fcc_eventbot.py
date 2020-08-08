import os
import discord
from dotenv import load_dotenv
import random
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

bot.run(TOKEN)

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#     # for guild in client.guilds:
#     #     for channel in guild.channels:
#     #         if type(channel) == discord.TextChannel:
#     #             print(channel.name)

# @client.event
# async def on_message(message):
#     if message.author != client.user:
#         await message.channel.send("SHHHH!!!!")

# client.run(TOKEN)