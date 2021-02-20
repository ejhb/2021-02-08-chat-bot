import discord
from discord.ext import commands
from datetime import datetime
from ftools import notify_user, mods_or_owner 
import pymongo
import pandas as pd

class Ratings(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_reaction_add(reaction, user):
        Channel = client.get_channel('812689170417713192')
        if reaction.message.channel.id != Channel:
            return
        if reaction.emoji == "🏃":
            Role = discord.utils.get(user.server.roles, name="Student")
            await client.add_roles(user, Role)


def setup(bot):
    bot.add_cog(Ratings(bot))