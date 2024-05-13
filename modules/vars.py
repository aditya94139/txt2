import os

api_id = int(os.environ.get("API_ID", '22334176'))
api_hash = os.environ.get("API_HASH", 'c68f6dfa9c118190c615bc54ba584a54')
bot_token = os.environ.get("BOT_TOKEN", '7185221162:AAHS9nRL-YuGINtSGYO6y_mc0pvOBqwcfdM')


OWNER = int(os.environ.get("OWNER", '1280494242'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", '1280494242').split(',')):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
