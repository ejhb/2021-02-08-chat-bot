import discord
from discord.ext import commands
import random
import time
from ftools import notify_user, mods_or_owner 
mods_or_owner 
class Feedback(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create_chan(self, ctx, channame: str ="" ):
        """
        This commands create a text channel.
        Parameters
        ----------
        !create_chan channelname
        """
        guild = ctx.message.guild
        await guild.create_text_channel(channame)

    @commands.command()
    async def delete_chan(self, ctx, given_name=None):
        """
        This commands delete a channel.
        Parameters
        ----------
        !delete_chan channelname
        """
        for channel in ctx.guild.channels:
            if channel.name == given_name:
                #get id = (not usefull yet)
                wanted_channel_id = channel.id
                await channel.delete()

    @commands.command()
    async def feedback(self , ctx):
        """
        This command allow you to send us a feedback. You will be redicted into a temp chan to gather your suggestions.
        Parameters
        ----------
        !feedback 
        """
        guild = ctx.message.guild
        happy_emoji = [":grinning:",":smiley:",":smile:",":grin:",":laughing:",":slight_smile:",":sunglasses:"]
        temp_chan = await guild.create_text_channel("feedback")
        temp_chan
        await ctx.send(f'We are ready to hear you about that in {temp_chan.mention}')
        await temp_chan.send(f'Welcome to you {ctx.author.mention} {random.choice(happy_emoji)}')
        await temp_chan.send(f'Are your ready to answers at my questions? (yes/no)')
        list_question = ["question_a","question_b","question_c","question_d"]
        list_answers = [] 
        msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        if msg.content.lower() == "yes":
            print("on est ici")
            # while len(self.list_question) >= 0:
            for question in list_question :
                await temp_chan.send(question)
                # self.list_question.remove(question)
                answers = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                list_answers.append(answers.content)
            await temp_chan.send("Thanks you for your feedback, we are about to close this channel")
            time.sleep(5)
            await notify_user(new_user, f'Thanks you for your feedback, we closed the channel.')
            await temp_chan.delete()
            print("L'utilisateur :",ctx.author,"voici ma liste de réponse :",list_answers)
        elif msg.content.lower() == "no":
            await temp_chan.send("Tu as dis no or n")
            await notify_user(ctx.author, f'You close the request')
            await temp_chan.delete()

        

   

def setup(bot):
    bot.add_cog(Feedback(bot))