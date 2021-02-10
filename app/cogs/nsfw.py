import discord
from discord.ext import commands
import random

import asyncio



class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "Roast someone")
    async def insult(self, ctx, member: discord.Member = None):
        insult = await get_momma_jokes()
        if member is not None:
            await ctx.send("%s  %s" %(member.name, insult))
        else : 
            await ctx.send(insult)


def setup(bot):
    bot.add_cog(NSFW(bot))
