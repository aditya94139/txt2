import os

api_id = int(os.environ.get("API_ID", '29251040'))
api_hash = os.environ.get("API_HASH", 'a1de34e4ad21cc9fb34798473eaf7bab')
bot_token = os.environ.get("BOT_TOKEN", '7185221162:AAHS9nRL-YuGINtSGYO6y_mc0pvOBqwcfdM')


OWNER = int(os.environ.get("OWNER", '1280494242'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", '1280494242').split(',')):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
