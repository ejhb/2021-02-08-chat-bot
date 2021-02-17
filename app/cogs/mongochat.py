import re
import html2markdown
import random

from discord.ext import commands
from data.list_pairs import pairs , reflections
# from cogs.botfeatures import BotFeatures

import nltk
from nltk.corpus import stopwords , wordnet as wn
from nltk import wordpunct_tokenize , WordNetLemmatizer
from nltk import word_tokenize
import string
from nltk.stem.snowball import SnowballStemmer
from nltk import ngrams

import pymongo


class Mongochat(commands.Cog):

    collDict = { "beer":"beer", "ia":"ia", "mechanics":"mechanics", "data_science":"data_science", "movies":"movies"}
    
    def __init__(self,bot, listen=True):
        """
        Initialize the chatbot.
        """
        self.bot = bot
        self.listen = listen

    @commands.command()
    async def toggler2(self , ctx, option: str = ""):
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

    def cleanhtml(self, raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

    def _lower(self, x, channel):
        n_message = x.lower() #change lettres to lower lettres
        t_message = word_tokenize(n_message) #tokenize
        exclude = set(string.punctuation) # detecter les signes de ponctuation 
        _stopwords = nltk.corpus.stopwords.words("english") #stop words
        _stopwords.extend(exclude) # rajouter les signes de ponctuation à la liste des stopwords
        tokens_without_stopwords = [word for word in t_message if word not in _stopwords]
        stemmer = SnowballStemmer("english")
        stem_message =set(stemmer.stem(token) for token in tokens_without_stopwords)
        stemmsg2 = []
        for it in stem_message:
            if str(it) != str(channel):
                stemmsg2.append(it)
            else:
                print("filtering out ", it)
        return ' '.join(stemmsg2)

    def _queryMongo(self, msg, channel):
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = client["homie"]
            posts = mydb[self.collDict[channel]]
            
            # {'$meta': 'textScore'} will add a 'score' to each result, and we sort using it:
            res = posts.find({'$text': {'$search': msg} },{'score': {'$meta': 'textScore'}}).sort([('score', {'$meta': 'textScore'})])
            # 'res' is a cursor, not a list, so we must iterate through it:
            listmot = msg.split()
            nb_de_mot = len(listmot)
            print(nb_de_mot)
            
            questlist = []
            scorelist = []
            
            for it in res:
                try:
                    questlist.append(it['AcceptedAnswerId'])
                    scorelist.append(it['score'])
                    score_m = scorelist[0]/nb_de_mot
                except:
                    print("No response found for: ", msg)
                    ""
            print("questlist:", questlist)
            print("questlist[0]",questlist[0])
            print("scorelist",scorelist)
            print("scorelist[0]",scorelist[0])
            print("Mean:",score_m) #pas moins de 0.4
        except:
            print("This chann is not related to discussion chatbot or word(s) not found")
            
        try:
            mongoresp = posts.find_one({"Id": questlist[0]})
            #print("score: ", mongoresp['score'])
            resp = mongoresp['Body']
        except:
            resp = ""
        return html2markdown.convert( resp )


    userrequests = {}
    
    def respond(self, msg, channel, user):
        if not channel in list(self.collDict.keys()):
            if msg.endswith("?"):
                self.userrequests[user] = msg
                tempresp = "What is the topic of your question? ("
                for it in list(self.collDict.keys()):
                    tempresp = tempresp + it + " "
                tempresp = tempresp.strip() + ")"
                return tempresp
            elif msg in list(self.collDict.keys()):
               oldmsg = self.userrequests[user]
               tokenized = self._lower(oldmsg, msg)
               return self._queryMongo( tokenized, msg )
            else:
                return ""
               
        else:
            tokenized = self._lower(msg, channel)
            if len(tokenized) > 0 and msg.endswith("?"):
                return self._queryMongo( tokenized, channel )
            else:
                return ""

    @commands.Cog.listener("on_message")
    async def mongoconverse(self, message):
        if self.listen is False :
            return
        elif self.listen is True:
            print("message.author: ", str(message.author))
            if message.author.bot or message.content.startswith('!'):
                return
            else:
                print("message.content: ", message.content)
                channel = str(message.channel)
                print("message.channel: ",channel)
                _response = self.respond(message.content, channel, message.author)
                if len(_response) > 0:
                    await message.channel.send( _response )
                else:
                    return
        
def setup(bot):
    bot.add_cog(Mongochat(bot))
