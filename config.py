import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "20369373"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "0d53cc7f978163fed3263be5cbb20ab0")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8958218005:AAF0akYDPpM1z3qLoDrJia5KgAvwZ6YE6DQ")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Hicwbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "8532700793"))
# ------------------X------------------------------
CREATOR_ID = int(os.environ.get("CREATOR_ID", "8532700793"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003990132795"))


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8532700793").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003990132795"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003990132795"))
