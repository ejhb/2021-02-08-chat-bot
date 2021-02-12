import discord
from discord.ext import commands

class BotFeatures(commands.Cog):
    def __init__(self, bot, listen):
        self.bot = bot
        self.listen = listen

    @commands.command()
    async def toggler(self , ctx, option: str = ""):
        """
        Toggle the listener function on or off.
        Parameters
        ------------
        !toggler "arg"
        """
        self.listen = False
        if option == "on":
            self.listen = True
            await ctx.send("Toggler has been set on")
            return self.listen 
        elif option == "off":
            self.listen = False
            await ctx.send("Toggler has been set off")
            return self.listen
        else:
            await ctx.send("Option must be on or off")

def setup(bot):
    bot.add_cog(BotFeatures(bot))