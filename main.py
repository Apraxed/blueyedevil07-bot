# import stuff
from keep_alive import keep_alive
import discord
from discord.ext import commands
import os
from config import config
import zbot

cfg = config

# creator
Creator = os.environ.get('Creator')

# Version number
Version = "Version 1.0.0"

# prefix
client = commands.Bot(command_prefix=cfg.BOT_PREFIX)

@client.event
async def on_ready():
  print(os.environ.get('start message'))
  print(client.user.name)
  print('online')
  channel = client.get_channel(741447869441245325)
  embed = discord.Embed(title = 'bot is online', description = f'Bot is online')
  await channel.send(embed = embed)
  await client.change_presence(activity=discord.Streaming(name=cfg.status, url=cfg.twitch_url))

# pp_size cmd from fun_commands.py
@client.command(pass_context = True, aliases = ['pp-size'])
async def pp_size(ctx):
    zbot.funcmds.pp_size

@client.command()
async def meme(ctx):
    zbot.funcmds.meme

@client.command()
async def randomnumbergen(ctx):
    zbot.funcmds.rng

@client.command()
async def rps(ctx):
    zbot.funcmds.rps

@client.command()
@commands.has_any_role('administrive', 'my fam')
async def tempban(ctx, member: discord.Member, reason = None):
    zbot.modcmds.tempban

@client.command
@commands.has_any_role('administrive', 'my fam')
async def permban(ctx, member: discord.Member, reason = None):
    zbot.modcmds.pban

@client.command()
@commands.has_any_role('administrive', 'my fam')
async def kick(ctx, member: discord.Member, reason = None):
    zbot.modcmds.kick

keep_alive()
client.run(cfg.TOKEN_ENV)