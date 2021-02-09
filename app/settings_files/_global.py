import os 

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR,'data')

DISCORD_TOKEN_PERSONNAL = os.getenv("DISCORD_TOKEN_PERSONNAL", False)

REDDIT_APP_ID = os.getenv("DISCORD_BOT_TOKEN", False)
REDDIT_APP_SECRET = os.getenv("DISCORD_BOT_TOKEN", False)