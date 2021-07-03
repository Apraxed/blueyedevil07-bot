import discord
from config import config

cfg = config
client = discord.Client
async def event_types():
    async def playing():
        await client.change_presence(activity=discord.Game(name=cfg.status))

    async def streaming():
        await client.change_presence(activity=discord.Streaming(name=cfg.status, url=cfg.twitch_url))

    async def listening():
         await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=cfg.status))

    async def watching():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config.status))