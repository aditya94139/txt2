import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "841021123").split()):
        ADMINS.append(int(x))
