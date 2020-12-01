import discord
from discord.ext import commands
import datetime

import os
import random
from dotenv import load_dotenv
import youtube_dl
import math
import random
import youtube_dl
from async_timeout import timeout



# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''

from urllib import parse, request
import re
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

load_dotenv()
players={}
bot = commands.Bot(command_prefix=',', description="Second half of Black Zetsu")

bot.remove_command("help")

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available.')
    embed.add_field(name=',ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name=',info', value='Random info stuff', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Second half of black Zetsu!", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    #embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(',help for a list of Commands'))
    print('My body is ready')

#Doing a music bot w/o understanding how discord.py works :monkas:

@bot.command(pass_context=True)
async def join(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await bot.join_voice_channel(channel)
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

#Some dumb shit that works for some reason

@bot.command(aliases=['gayness'])
async def gay(ctx, *, question):
    responses = ["LOL YOU GAY XDDD FUNNY",
                    "HOMO ALERT",
                    "MY GAY-SENSOR IS OFF THE CHARTS",
                    "STINKY GAY",
                    "BIG GEAY",
                    "THE SOCKS ARE OFF",
                    "HELLA GAY"
                    "Possible homo",
                 "My gay-sensor is picking something up",
                 "I can't tell if the socks are on or off",
                 "Gay-ish",
                 "Looking a bit homo",
                 "lol half  g a y",
                 "safely in between for now",
                 "No homo",
                 "Wearing socks",
                 '"Only sometimes"',
                 "Straight-ish",
                 "No homo bro",
                 "Girl-kisser",
                 "Hella straight"
                 ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')





#Note to myself: DONT FUCKING TOUCH THIS

with open("token.txt") as f:
  token = f.read()
bot.run(token)