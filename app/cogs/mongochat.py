import re
import html2markdown
#import random

from discord.ext import commands
#from data.list_pairs import pairs , reflections
# from cogs.botfeatures import BotFeatures

import nltk
#from nltk.corpus import stopwords , wordnet as wn
#from nltk import wordpunct_tokenize , WordNetLemmatizer
from nltk import word_tokenize
import string
from nltk.stem.snowball import SnowballStemmer
#from nltk import ngrams

import pymongo


class Mongochat(commands.Cog):

    collDict = { "beer":"beer", "ia":"ia", "mechanics":"mechanics", "data_science":"data_science", "movies":"movies"}
    
    def __init__(self,bot, listen=True):
        """
        Initialize the chatbot.
        """
        self.bot = bot
        self.listen = listen

    # @commands.command()
    # async def toggler2(self , ctx, option: str = ""):
    #     """
    #     Toggle the listener function on or off.
    #     Parameters
    #     ------------
    #     !toggler "arg"
    #     """
    #     self.listen = False
    #     if option == "on":
    #         self.listen = True
    #         await ctx.send("Toggler has been set on")
    #         return self.listen 
    #     elif option == "off":
    #         self.listen = False
    #         await ctx.send("Toggler has been set off")
    #         return self.listen
    #     else:
    #         await ctx.send("Option must be on or off")

    def _cleanhtml(self, raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

    def _lower(self, msg, channel):
        if msg == "yes" or msg == "y" or msg == "no" or msg == "n":
            return msg
        
        n_message = msg.lower() #change lettres to lower lettres
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

    stockage_premier_phrase = {}
    def _queryMongo(self, msg, channel, user):
        print("MSG-_queryMg: ", msg)
 
        if msg == "yes":
            if user in list(self.stockage_premier_phrase.keys()):
                return self.stockage_premier_phrase[user]
            else:
                return "Yes?"
        elif msg == "no":
            return "No?"
        else:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = client["homie"]
            posts = mydb[self.collDict[channel]]
            
            # {'$meta': 'textScore'} will add a 'score' to each result, and we sort using it:
            res = posts.find({'$text': {'$search': msg} },{'score': {'$meta': 'textScore'}}).sort([('score', {'$meta': 'textScore'})])
            
            nb_de_mot = len(msg.split())
            questlist = []
            scorelist = []
            taglist = []
            score_m = 0
            
            print("MSG-_query-else: ", msg)
            for it in res:
                try:
                    questlist.append(it['AcceptedAnswerId'])
                    scorelist.append(it['score'])
                    score_m = scorelist[0]/nb_de_mot
                    tags = it['Tags']
                    tags = tags.strip('<>').replace('><', ' ') 
                    taglist.append(tags)
                    mongoresp = posts.find_one({"Id": questlist[0]})
                    self.stockage_premier_phrase[user] = mongoresp['Body']
                except:
                    #print("No response found for: ", msg)
                    ""
            print("questlist: ", questlist)
            print("scorelist: ",scorelist)
            print("Mean: ",score_m) #pas moins de 0.4
            print("taglist: ",taglist)
            
            try:
                resp = posts.find_one({"Id": questlist[0]})['Body']
            except:
                return "Could not find ans answer on topic " + channel
            if score_m > 1.5:
                return html2markdown.convert( resp )
            elif score_m > 0.4:
                
                return "Did your question concern " + str(taglist) + "?"
            else:
                return "Could not find ans answer on topic " + channel


    userrequests = {}
    def respond(self, msg, channel, user):
        print("MSG-respond: ", msg)
        if not channel in list(self.collDict.keys()):
            if msg == "yes" or msg == "y" or msg == "no" or msg == "n":
                return self._queryMongo( self._lower(msg, channel), msg, user )
            elif msg.endswith("?"):
                self.userrequests[user] = msg
                tempresp = "What is the topic of your question? ("
                for it in list(self.collDict.keys()):
                    tempresp = tempresp + it + " "
                tempresp = tempresp.strip() + ")"
                return tempresp
            elif msg in list(self.collDict.keys()):
               print("MSG-respond-is-channel: ", msg)
               oldmsg = self.userrequests[user]
               tokenized = self._lower(oldmsg, msg)
               return self._queryMongo( tokenized, msg, user )
            else:
                print("MSG-respond-unsupported")
                return ""
        elif msg.endswith("?"):
            tokenized = self._lower(msg, channel)
            if len(tokenized) > 0:
                return self._queryMongo( tokenized, channel, user )
            else:
                return "emptyquestion"
        else:
            return "notaqquestion"

    @commands.Cog.listener("on_message")
    async def mongoconverse(self, message):
        print("MSG-mongoconverse: ", message.content)
        if self.listen is False :
            return
        elif self.listen is True:
            if message.author.bot or message.content.startswith('!'):
                return
            else:
                print("MSG-mongoconverse-else: ", message.content)
                channel = str(message.channel)
                _response = self.respond(message.content, channel, message.author)
                if len(_response) > 0:
                    await message.channel.send( _response )
                else:
                    return
        
def setup(bot):
    bot.add_cog(Mongochat(bot))