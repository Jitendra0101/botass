import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("bot is up for shit")

@client.command()
async def hello(ctx):
    await ctx.send("hey there punk")

@client.command()
async def stfu(ctx):
    await ctx.send("no you shut the fuck up whore")

@client.command()
async def f(ctx):
    await ctx.send("pay respect")

@client.command()
async def bruh(ctx):
    await ctx.send("bruh moment certified")
    
client.run(os.environ['token'])
