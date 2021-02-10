from discord.ext import commands
import random


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "Roll rand numb 1 to 100")
    async def roll(self, ctx):
        n = random.randrange(1, 101)
        await ctx.send(n)

    @commands.command(brief = "Dice rand numb 1 to 6")
    async def dice(self, ctx):
        n = random.randrange(1, 7)
        await ctx.send(n)

    @commands.command(brief = "Toss a coin for your witcher")
    async def coin(self, ctx):
        n = random.randint(0, 1)
        await ctx.send("Pile" if n == 1 else "Face")

def setup(bot):
    bot.add_cog(Gamble(bot))
