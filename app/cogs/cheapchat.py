import re
import random

from discord.ext import commands
from data.list_pairs import pairs , reflections
# from cogs.botfeatures import BotFeatures


class Cheapchat(commands.Cog):
    def __init__(self,bot, pairs=pairs, reflections=reflections, listen=False):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()
        self.bot = bot
        self.listen = listen


    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match): #wildcards = (.*)
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                return resp

    @commands.command()
    async def cheap(self , ctx, option: str = ""):
        """
        Toggle the listener function on or off.
        Parameters
        ------------
        !cheap on/off
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

    @commands.Cog.listener("on_message")
    async def converse(self, message):
        if self.listen is False :
            return
        elif self.listen is True :
            if message.author.bot:
                return
            else:
                user_input = message.content
                await message.channel.send(self.respond(user_input))

        #while user_input != quit:
        #    user_input = quit
        #    try:
        #       user_input = input(">")
        #    except EOFError:
        #        await ctx.send(user_input)
        #    if user_input:
        #        while user_input[-1] in "!.":
        #            user_input = user_input[:-1]
        #        await ctx.send(self.respond(user_input))
        
def setup(bot):
    bot.add_cog(Cheapchat(bot))
