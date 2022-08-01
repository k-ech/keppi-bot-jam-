from discord.utils import get
from discord.ext import commands
import os


client = commands.Bot(command_prefix="! ", help_command = None)



@client.event
async def on_ready():
    print("readying..... ready!")


@client.command(aliases=["hi","HELLO","Hello","Hi"])
async def hello(ctx):
    await ctx.send("Hello")


client.run("MTAwMzc0MDQyMzQ2MzkwMzIzMw.GPbXFU.edtknEHrabHAFlAGjvHkbBfOQRb7HTP5WY0wbc")
