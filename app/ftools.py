import random
import json
import os
import importlib

from settings import * 


async def get_momma_jokes():
    with open(os.path.join(DATA_DIR,"jokes.json")) as joke_file:
        jokes = json.load(joke_file)
    random_category = random.choice(list(jokes.keys()))
    insult = random.choice(list(jokes[random_category]))
    return insult


# def import_list_lair():
#     pair_file = open(os.path.join(DATA_DIR,"list_pairs.py")) 
#     return pairs

# print(pair_file.read())