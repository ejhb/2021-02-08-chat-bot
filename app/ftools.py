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

def mods_or_owner():
    """
    Check that the user has the correct role to execute a command
    """
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(MODERATOR_ROLE_NAME))
    return commands.check(predicate)


# def import_list_lair():
#     pair_file = open(os.path.join(DATA_DIR,"list_pairs.py")) 
#     return pairs

# print(pair_file.read())