from discord.ext import commands
import discord

from ftools import mods_or_owner

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason: str = "Because you were bad. We kicked you."):
        """A command which ban a register member
        Parameters
        ------------
        !kick @user "reason"
        """
        if member is not None:
            await ctx.guild.kick(member, reason=reason)
        else:
            await ctx.send("Please specify user to kick via mention")
    
    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = "Because"):
        """A command which ban a register member
        Parameters
        ------------
        !ban @user "reason"
        """
        if member is not None: 
            await ctx.guild.ban(member, reason=reason)
        else:
            await ctx.send("Please specify user via mention")
    
    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, member: str ="", reason: str = "Because"):
        """A command which unban user from ban list
        Parameters
        ------------
        !unban username
        """
        if member == "": 
            await ctx.send("Please specify user via mention")
            return
        
        bans = await ctx.guild.bans()
        for b in bans: 
            if b.user.name == member:
                await ctx.guild.unban(b.user, reason=reason)
                await ctx.send(f'User has been unbanned')
                return
        await ctx.send("User not found in ban list.")

def setup(bot):
    bot.add_cog(Moderator(bot))