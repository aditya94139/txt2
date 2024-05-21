import os

api_id = int(os.environ.get("API_ID", '23291931'))
api_hash = os.environ.get("API_HASH", '4b11dd648188731fb7c9bc8083e8791c')
bot_token = os.environ.get("BOT_TOKEN", '7078804290:AAEOgiUjc9tzMte1SBepRZII6cRizz6Bysg')


OWNER = int(os.environ.get("OWNER", '6594402123'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", '6594402123').split(',')):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
