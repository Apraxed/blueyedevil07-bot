from cogs import fun_commands, moderation_commands, modmail, needs_owner_perms, game_commands
import discord

async def modcmds(ctx, member: discord.Member, reason = None):
    async def tempban(ctx, member: discord.Member, reason = None):
        moderation_commands.temp_ban10d
    async def pban(ctx, member: discord.Member, reason = None):
        moderation_commands.permban
    async def kick(ctx, member: discord.Member, reason = None):
        moderation_commands.kick
    async def userreports(message):
        modmail.modmail
    async def purge(ctx):
        moderation_commands.purge

async def funcmds(ctx):
    async def meme(ctx):
        fun_commands.meme
    async def pp_size(ctx):
        fun_commands.pp_size
    async def randomnumgen(ctx):
        fun_commands.rng

async def ifmisusseditviolatestos():
    async def areyousure():
        async def youreallyaredoingthis():
            async def idkwhytho():
                async def emojis():
                    needs_owner_perms.deleteemojis
                async def channels():
                    needs_owner_perms.deletechannels

async def games():
    async def rps():
        game_commands.rps
    async def casino():
        game_commands.casino