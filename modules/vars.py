import os

api_id = int(os.environ.get("API_ID", '24537816'))
api_hash = os.environ.get("API_HASH", 'd88c4e65689faa570fbc5949468b5c61')
bot_token = os.environ.get("BOT_TOKEN", '7002079043:AAHXx-wKS4qKYezsUOWgUlzy2Cgz4qgA3JA')


OWNER = int(os.environ.get("OWNER", '5827915041'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", '1368753935').split(',')):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
