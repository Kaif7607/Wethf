import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "29426008"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "fedd630ba4bd77044ee4e5a00e5300e6")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8464006684:AAHfz3jFQCaijVmG353odA9B90t-7-_Z2JE")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("J_geobot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1717411093"))
# ------------------X------------------------------
CREATOR_ID = int(os.environ.get("CREATOR_ID", "1717411093"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003549344180"))


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1717411093").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003549344180"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://jilanirabbani1234_db_user:Jil%40ni7417@mondb.cxuaxsk.mongodb.net/?appName=Mondb")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003549344180"))
