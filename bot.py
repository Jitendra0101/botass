import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("bot is online")

@client.command()
async def hello(ctx):
    await ctx.send("hey there punk")

@client.command()
async def love(ctx):
    await ctx.send("<3 <3 <3")

@client.command()
async def f(ctx):
    await ctx.send("pay respect")

@client.command()
async def bruh(ctx):
    await ctx.send("bruh moment certified")
    
client.run(os.environ['token'])
