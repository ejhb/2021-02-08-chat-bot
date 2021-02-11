import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener("on_message")
    async def greet(self, message):
        print('Message from {0.author}:{0.content}'.format(message))

        if message.content == "bouffon" :
            await message.channel.send("So young to be a buffoon", tts=True)
        if message.content == "dan evil":
            await message.channel.send("Dan is a evil worshiper", tts=True)
            
def setup(bot):
    bot.add_cog(Misc(bot))