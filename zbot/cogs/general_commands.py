import discord 
from discord.ext import commands
from asyncio.tasks import sleep
import aiohttp
import random


client = commands.Bot(command_prefix='', help_command=None)

async def latency_cmd(ctx):
    ping = int(round(client.latency, 3) * 1000)
    await ctx.send(f'<@{ctx.author.id}> {ping} ms.')