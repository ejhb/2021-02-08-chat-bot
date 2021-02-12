from discord.ext import commands
import random


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'roll',brief = "Roll rand numb 1 to 100")
    async def roll(self, ctx):
        """A simple command which pick a number between 1 and 100."""
        n = random.randrange(1, 101)
        await ctx.send(n)

    @commands.command(brief = "Dice rand numb 1 to 6")
    async def dice(self, ctx):
        """A simple command which roll a sixth side dice."""
        n = random.randrange(1, 7)
        await ctx.send(n)

    @commands.command(brief = "Toss a coin")
    async def coin(self, ctx):
        """Toss a coin for your witcher."""
        n = random.randint(0, 1)
        await ctx.send("Pile" if n == 1 else "Face")

def setup(bot):
    bot.add_cog(Gamble(bot))
