import discord
import traceback
import sys
from discord.ext import commands


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
     ## command error feedback
    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        if isinstance(ex, CommandNotFound):
            await ctx.send("Unfortunately we failed to find your command please refer to !help")
        elif hasattr(ex,"original"):
            raise ex.original
        else : 
            raise ex
        # await ctx.send(f'What do you mean by {ex.original} ? \nPlease check with !help, or on the manual at trucGithub.com')

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))