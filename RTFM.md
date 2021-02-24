INEEDAHOMIE

Brief fin de bloc 2: 

Répartition du rôle du Scrum Master:

Jour
Cécilia
Wiem
Dan
Julien
Joshua
Lundi 8/2/21




x




Mardi 9/2/21




x




Mercredi 10/2/21






x


Jeudi 11/2/21






x


Vendredi 12/2/21








x












Lundi 15/2/21








x
Mardi 16/2/21
x








Mercredi 17/2/21
x








Jeudi  18/2/21


x






Vendredi 19/2/21


x


















Lundi 21/2/21


x










Liens utiles:

Trello: https://trello.com/b/0giCfh1T/chatbot 
Planning Poker: https://www.scrumpoker-online.org/
Github: https://github.com/ejhb/2021-02-08-chat-bot
Burn Down Chart: https://docs.google.com/spreadsheets/d/1uWuBJ9mF5zQbF-SfeKCdTlduz3t49Pp8tox1NlsQ9EM/edit?usp=sharing


https://archive.org/download/stackexchange

https://github.com/Rapptz/discord.py

https://discordpy.readthedocs.io/en/latest/discord.html

https://www.kdnuggets.com/2019/05/build-chatbot-python-nltk.html

https://chatterbot.readthedocs.io/en/stable/tutorial.html

https://docs.mongodb.com/manual/text-search

























Data Dump stackexchange

Un datadump SE est constitué de 2 archives, celle avec le contenu propre plus une 'meta'. Chacune des archive contient la même liste de fichiers : Badges.xml, Comments.xml, PostHistory.xml, PostLinks.xml, Posts.xml, Tags.xml, Users.xml, Votes.xml.
A priori seul Posts.xml nous intéresse : ce fichier contient tous les posts d'un stack qu'ils soient une question (PostTypeId="1") ou une réponse (PostTypeId="2"). Chaque entrée 'question' contient un AcceptedAnswerId qui est l'ID du post accepté comme réponse (chaque post réponse contient aussi un ParentId qui référence le post question).

Exemple de post question :
  <row Id="1" PostTypeId="1" AcceptedAnswerId="4" CreationDate="2014-01-21T20:26:05.383" Score="20" ViewCount="2346" Body="&lt;p&gt;I was offered a beer the other day that was reportedly made with citra hops. What are citra hops? Why should I care that my beer is made with them?&lt;/p&gt;&#xA;" OwnerUserId="7" LastEditorUserId="8" LastEditDate="2014-01-21T22:04:34.977" LastActivityDate="2014-01-21T22:04:34.977" Title="What is a citra hop, and how does it differ from other hops?" Tags="&lt;hops&gt;" AnswerCount="1" CommentCount="0" ContentLicense="CC BY-SA 3.0" />

Exemple de post réponse :
  <row Id="4" PostTypeId="2" ParentId="1" CreationDate="2014-01-21T20:31:18.540" Score="14" Body="&lt;p&gt;Citra is a registered trademark since 2007. Citra Brand hops have fairly high alpha acids and total oil contents with a low percentage of cohumulone content and  imparts interesting citrus and tropical fruit characters to beer.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;For more information, you can read the &lt;a href=&quot;http://en.wikipedia.org/wiki/List_of_hop_varieties#Citra_brand_HBC_394_cv&quot;&gt;Wikipedia article&lt;/a&gt; on the Citra brand.&lt;/p&gt;&#xA;" OwnerUserId="12" LastEditorUserId="25" LastEditDate="2014-01-21T21:36:38.133" LastActivityDate="2014-01-21T21:36:38.133" CommentCount="0" ContentLicense="CC BY-SA 3.0" />

Pour le bot (et donc la DB), on aura juste besoin des attributs Id, PostTypeId, AcceptedAnswerId, et Body. Les autres attributs peuvent être ignorés. Lorsqu'une question est posée, le bot cherche la question équivalente dans l'ensemble des post taggés  PostTypeId="1", puis affichera la réponse trouvée dans AcceptedAnswerId.
Note : le Body de chaque entrée est en HTML, il faudra donc filtrer les &lt; &gt; etc…


4. Transformation XML -> JSON

Code python pour traduire un fichier Posts.xml extrait du datadump SE en fichier JSON:

import xmltodict
import pprint
import json

with open('Posts.xml') as fd:
    doc = xmltodict.parse(fd.read())

json_data = json.dumps(doc)

with open("Posts.json", "w") as json_file:
        json_file.write(json_data)



5- Création bot sur discord

https://discord.com/developers/applications
-connection
-new application
-lui donner un nom
-bot #sur la gauche
-add bot
-coche permission liste:
gérer les rôle
gérer les salons
changer le pseudo
gerer les émojis
lire les messages
envoyer des messages
envoyer des messages tts
gérer les messages
intégrer les liens
joindre des fichiers
voir les anciens messages
mentionner@..
Ajouter des réactions
utiliser des émojis externes
se connecter
parler
-décoche public bot
-copie tokenkey
-dans Oauth2 sélectionne bot
-copie l'url et coller dans moteur de recherche
-sélectionne le serveur


-cloner les documents dans le dossier du brief
git clone https://github.com/ejhb/2021-02-08-chat-bot.git
-git branch
-git pull
-git pull origin master
-git status





création nouvel environnement:
-conda create --name homie
-conda activate homie

installation de ce qu'il faut dans l'environnement
-conda install --c
-conda install -c anaconda pip
-pip install -r requierements.txt  #install ce qui se trouve dans le requirement

-ouvrir vscode dans cet environnement
-ouvrir le doss avec le fichier cloné
-creation fichier tokenkey.py et y mettre:
tokenkey= #coller la clef copiée dans bot, token
-si création d'un workspace le collé dans le gitignore



Installation de son docker MongoDB:

Installer un conteneur mongodb:(optionnel)

sudo apt install docker.io
sudo docker run -d -p 27017:27017 -v ~/src/data/mongo-docker:/data/db --name mongodb mongo:4.2

Créer un répertoire de travail: 

Dans le répertoire de travail, on crée un répertoire pour la base de données datasets/

Lister ou vérifier le nom du conteneur adéquat : sudo docker ps -a

Démarrage du container mongodb : sudo docker start mongodb

Exécution de mongodb : ibz

Création de la base : use nomdebase;

Donne le nom de la base :  db;

Création user :  db.createUser({
user : “nom”
pwd: “motdepass”
roles: [“readwrite”, “dbadmin”]});  

Création de la table : db.createCollection(‘nomtable’);  

    10. Insertion dans la table : db.nomdetable.insert([{nom: “doe”, prenom:         ”john"}]);

    11.  Renvoi info table : db.nomdetable.find().pretty()

    12. Mettre à jour, ex tous ceux qui on le nom “saint” aurons la ligne “sexe: femme” en plus :     db.nomdetable.update({nom: “saint”}, {$set:{sexe:”femme”}}) 

    13. Commandes python pour pymongo:  

import pymongo
from pymongo import MongoClient
connection = MongoClient()
db = connection.nomdelabase
collection = db.nomdelatable

Import du fichier postsBeer2.json (à télécharger sur le Trello ds Ressources)

sudo docker exec -it mongodb mongo 

sudo docker cp PostsBeer2.json mongodb:/tmp/posts.json # On doit copier le fichier ds le rep connu par le docker de mongoDB ici /tmp/

sudo docker exec mongodb mongoimport -d <db-name> -c posts --file /tmp/posts.json

sudo docker exec mongodb mongoimport -d homie -c posts --file /tmp/posts.json --jsonArray

Le résultat de votre terminal devrait être cela
“2021-02-10T11:04:44.669+0000    connected to: mongodb://localhost/
2021-02-10T11:04:45.106+0000    3579 document(s) imported successfully. 0 document(s) failed to import.”

Commentaires de modification sur json : (plus à faire)

Prétraitement (à la main) du json; Le début du fichier doit ressembler à cela

“[
      {
        "Id": "1", 
        "PostTypeId": "1",
        "AcceptedAnswerId": "4",

#la bdd n’est pas correctement lisible pour le moment
#j’ai réduit d’un niveau le json comme ce qui suit:
“[
      {
        "Id": "1", 
        "PostTypeId": "1",
        "AcceptedAnswerId": "4",
        "CreationDate": "2014-01-21T20:26:05.383",
        "Score": "20",
        "ViewCount": "2346",
[…]”


MongoDB Queries From Python

# In MongoDB (assuming 'homie' is the DB's name):
# use homie
# db.posts.createIndex({Title:"text"})

#In Python:
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["homie"]
posts = mydb["posts"]

mdbquery = "citra hops" # Replace with yout text query

# {'$meta': 'textScore'} will add a 'score' to each result, 
# and we sort using it:
res = posts.find({'$text': {'$search': mdbquery} },{'score': {'$meta': 'textScore'}}).sort([('score', {'$meta': 'textScore'})])
# 'res' is a cursor, not a list, so we must iterate through it:
questlist = []
for it in res:
    try:
    #print(it['AcceptedAnswerId'])
    questlist.append(it['AcceptedAnswerId'])
    except:
    ""
#print(questlist)
resp = posts.find_one({"Id": questlist[0]})
print(resp['Body'])


Ameliorations possibles:
Gestion tags
Recherche : utiliser Snowball dans MongoDB ?


8. NLP function:
#import librairies
from nltk.corpus import stopwords , wordnet as wn
from nltk import wordpunct_tokenize , WordNetLemmatizer
from nltk import word_tokenize
import string
from nltk.stem.snowball import SnowballStemmer
from nltk import ngrams
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

#define your message
x = ‘your message’
#the NLP function
def lower(x):
    n_message = x.lower() #change lettres to lower lettres
    t_message = word_tokenize(n_message) #tokenize
    exclude = set(string.punctuation) # detecter les signes de ponctuation 
    stopwords = nltk.corpus.stopwords.words("english") #stop words
    stopwords.extend(exclude) # rajouter les signes de ponctuation à la liste des stopwords
    tokens_without_stopwords = [word for word in t_message if word not in stopwords]
    #lemma = WordNetLemmatizer()
    stemmer = SnowballStemmer("english")
    stem_message =set(stemmer.stem(token) for token in tokens_without_stopwords)
    original = ' '.join(stem_message)
    #bigrams = ngrams(stem_message,2)
    #for i in  bigrams:
    #    print(i)
    return original
# call function
lower(x)


9. Veille

Machine Learning:

SVM(le meilleur mais long avec les grosses bdd), 
Naïves Bayes, 
Decision Trees

Deep learning:

https://realpython.com/python-keras-text-classification/
https://code.google.com/p/word2vec/
http://nlp.stanford.edu/projects/glove/

API Keras

TensorFlow (Google) => classification de texte https://www.tensorflow.org/tutorials/text/text_classification_rnn

Theano

CNTK - ONNX (Micro$oft)

Exemple de mise en œuvre du NLP avec Keras & TensorFlow


10. Restitution client du lundi 15/02

11. Import de plusieurs bases de données dans des collections associées à celles-ci (US2) 
Wiem&Julien doivent apporter celles-ci en JSON de manière identique à postsBeer2 (objects contenus dans un tableau)

Démarrage de Docker à froid
sudo docker start mongodb
sudo docker exec -it mongodb mongo 

Copie des BDD dans le Docker
# On doit copier les fichiers ds le rep connu par le docker de mongoDB ici /tmp/
sudo docker cp movies.json mongodb:/tmp/movies.json 

Importation
b
gochat.py
Le résultat de votre terminal devrait être cela : x document(s) imported successfully. 0 document(s) failed to import



12. Créer de nouvelles fonctions dans MongoChat.py

Recherche multi-bases

13. MongoDB search

MongoDB: 
db.beer.find({"Tags" : "<drinking>"}) #Search by exact keyword
db.beer.find({"Tags" : {$regex:'drinking'}}) #Search with partial keyword







def _queryMongo(self, msg, channel):
       client = pymongo.MongoClient("mongodb://localhost:27017/")
       mydb = client["homie"]
       posts = mydb[self.collDict[channel]]
      
       mdbquery = msg # Replace with your text query
      
       # {'$meta': 'textScore'} will add a 'score' to each result, and we sort using it:
       res = posts.find({'$text': {'$search': mdbquery} },{'score': {'$meta': 'textScore'}}).sort([('score', {'$meta': 'textScore'})])
 
 
       listmot = msg.split()
       nb_de_mot = len(listmot)
       print(nb_de_mot)
 
      
       # 'res' is a cursor, not a list, so we must iterate through it:
       questlist = []
       scorelist = []
       for it in res:
           try:
               questlist.append(it['AcceptedAnswerId'])
               print("questlist[0]:",questlist[0])
               scorelist.append(it['score'])
               print("scorelist[0]:",scorelist[0])
               score_m = scorelist[0]/nb_de_mot
               print("score_m",score_m) #pas moins de 0.4                  
 
           except:
              
               #print("No response found for: ", msg)
              
               ""
       try:
           if score_m > 0.4:
               mongoresp = posts.find_one({"Id": questlist[0]})
               #print("score: ", mongoresp['score'])
               resp = mongoresp['Body']
           else:
               erreur = "i don't have a pertinent respond, sorry :( !"
               return (erreur)
       except:
           resp = ""
 
 
       return html2markdown.convert( resp )
  


Dan:
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["homie"]
posts = mydb[self.collDict[channel]]
      
mdbquery = msg # Replace with your text query
      
# {'$meta': 'textScore'} will add a 'score' to each result, and we sort using it:
res = posts.find({'$text': {'$search': mdbquery} },{'score': {'$meta': 'textScore'}}).sort([('score', {'$meta': 'textScore'})])
# 'res' is a cursor, not a list, so we must iterate through it:
              
 
questlist = []
taglist = []
      
for it in res:
try:
              questlist.append(it['AcceptedAnswerId'])
             tags = it['Tags']
             tags = tags.strip('<>').replace('><', ' ')
             questlist.append(tags)
             print("TAGS:", tags)
              
           except:
               #print("No response found for: ", msg)
               ""
       try:
           mongoresp = posts.find_one({"Id": questlist[0]})
           print("*******", mongoresp['Tags'])
           resp = mongoresp['Body']
       except:
           resp = ""
       return html2markdown.convert( resp )

Drop coll Index:
db.beer.dropIndex("Title_text")

Create coll multi indexes:
db.beer.createIndex({"Title":"text","Tags":"text"})

Show indexes:
db.beer.getIndexes()



A faire( 21/02):
  
13.5 
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["homie"]

question1_content = "Aimes tu les pâtes ?"
question2_content = "Aimes tu le bonne sousoupe ?"
question3_content = "Aimes tu pymongo ?"
question4_content = "Homie le giga bro"

question ={
    "question1":question1_content,
    "question2":question2_content,
    "question3":question3_content,
    "question4":question4_content
}

mydb.create_collection("user")
mydb.create_collection("question")
mydb.question.insert_one(question)


14. Copie des jsons sur MongoDB Atlas

Copie des JSON dans Docker:(si pas déjà réalisé)

sudo docker cp beer2.json mongodb:/tmp/beer2.json
sudo docker cp mechanics2.json mongodb:/tmp/mechanics2.json
sudo docker cp ia2.json mongodb:/tmp/ia2.json
sudo docker cp data_science2.json mongodb:/tmp/data_science2.json
sudo docker cp movies2.json mongodb:/tmp/movies2.json

Copie des JSON à distance

sudo docker exec mongodb mongoimport --uri "mongodb+srv://homie:a1b2c3@cluster0.n1mge.mongodb.net/homie" --collection beer --drop --file /tmp/beer2.json --jsonArray

sudo docker exec mongodb mongoimport --uri "mongodb+srv://homie:a1b2c3@cluster0.n1mge.mongodb.net/homie" --collection ia --drop --file /tmp/ia2.json --jsonArray

sudo docker exec mongodb mongoimport --uri "mongodb+srv://homie:a1b2c3@cluster0.n1mge.mongodb.net/homie" --collection data_science --drop --file /tmp/data_science2.json --jsonArray

sudo docker exec mongodb mongoimport --uri "mongodb+srv://homie:a1b2c3@cluster0.n1mge.mongodb.net/homie" --collection movies --drop --file /tmp/movies2.json --jsonArray

sudo docker exec mongodb mongoimport --uri "mongodb+srv://homie:a1b2c3@cluster0.n1mge.mongodb.net/homie" --collection mechanics --drop --file /tmp/mechanics2.json --jsonArray


IMPORT DES COLLECTIONS USER et QUESTION

pip install dnspython

#fichier xyz.py
import pymongo, dns
 
# client = pymongo.MongoClient("mongodb://localhost:27017/")
client = pymongo.MongoClient("mongodb+srv://homie:a1b2c3@cluster0.n1mge.mongodb.net/homie")
mydb = client["homie"]
 
question1_content = "Aimes tu les pâtes ?"
question2_content = "Aimes tu le bonne sousoupe ?"
question3_content = "Aimes tu pymongo ?"
question4_content = "Homie le giga bro"
 
question ={
   "question1":question1_content,
   "question2":question2_content,
   "question3":question3_content,
   "question4":question4_content
}
 
mydb.create_collection("user")
mydb.create_collection("question")
 
mydb.question.insert_one(question)

Création des index:
sudo docker exec -it mongodb mongo "mongodb+srv://cluster0.n1mge.mongodb.net/homie" --username homie

db.data_science.createIndex({Title:"text"})
db.movies.createIndex({Title:"text"})
db.ia.createIndex({Title:"text"})
db.beer.createIndex({Title:"text"})
db.mechanics.createIndex({Title:"text"})


Lancement de la BDD distante
sudo docker exec -it mongodb mongo "mongodb+srv://homie:a1b2c3@cluster0.n1mge.mongodb.net/homie" --username homie


Nltk pour heroku
Mettre les modules nltk necéssaire dans un fichier texte nltk.txt et le placer au meme niveau que le main.PY


15. Heroku
                   
heroku login                   
git status
git add .
git commit -m "creation compte heroku"
git push
heroku create your-application-namehe
git push heroku main?





mongoimport --uri "mongodb+srv://joshua:azerty123@homiedb.skyhb.mongodb.net/homie" --collection beer --drop --file beer2.json --jsonArray
mongoimport --uri "mongodb+srv://joshua:azerty123@homiedb.skyhb.mongodb.net/homie" --collection ia --drop --file ia2.json --jsonArray
mongoimport --uri "mongodb+srv://joshua:azerty123@homiedb.skyhb.mongodb.net/homie" --collection data_science --drop --file data_science2.json --jsonArray
mongoimport --uri "mongodb+srv://joshua:azerty123@homiedb.skyhb.mongodb.net/homie" --collection movies --drop --file movies2.json --jsonArray
mongoimport --uri "mongodb+srv://joshua:azerty123@homiedb.skyhb.mongodb.net/homie" --collection mechanics --drop --file mechanics2.json --jsonArray


import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://joshua:azerty123@homiedb.skyhb.mongodb.net/")
mydb = client["homie"]

question1_content = "Aimes tu les pâtes ?"
question2_content = "Aimes tu le bonne sousoupe ?"
question3_content = "Aimes tu pymongo ?"
question4_content = "Homie le giga bro"

question ={
    "question1":question1_content,
    "question2":question2_content,
    "question3":question3_content,
    "question4":question4_content
}

mydb.create_collection("user")
mydb.create_collection("question")

mydb.question.insert_one(question)