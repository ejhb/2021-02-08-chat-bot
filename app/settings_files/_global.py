import os 

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR,'data')

DISCORD_TOKEN_PERSONNAL = os.getenv("DISCORD_TOKEN_PERSONNAL", False)

REDDIT_APP_ID = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = os.getenv("REDDIT_APP_SECRET", False)
REDDIT_ENABLED_MEME_SUBREDDITS = [
    'funny',
    'memes',
    'wtf',
    'atbge',
    'beamazed',
    'nextfuckinglevel',
    'earthporn'
]
REDDIT_ENABLED_NSFW_SUBREDDITS = [
    'nsfw'
]