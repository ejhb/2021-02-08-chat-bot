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
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                if channel.name == "ratings":
                    self.channel = channel
                    self.msg_role = await self.channel.send("react with : :person_running:")
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message.id == self.channel

    @commands.command()
    async def oui(self,ctx):
        await self.channel.send('piou') 
                


def setup(bot):
    bot.add_cog(Ratings(bot))