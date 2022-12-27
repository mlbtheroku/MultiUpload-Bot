import os

class Config(object):
   # The Telegram API things
   API_ID= int(os.environ.get("API_ID", 17894641))
   API_HASH = os.environ.get("API_HASH", "4e5b39e5c7c6066e5144dfc50cf466cf")
   # get a token from @BotFather
   BOT_TOKEN = os.environ.get("BOT_TOKEN", "5823556553:AAHQgarPyBdfxpc9UcEuorb49dGDM0m_b4c")
   # channel id = -100 (for logs)
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001705637043"))   
   # Array to store users who are authorized to use the bot 
   AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5468192421").split())    
   # force sub user to the channel (without @)
   CHNAME = os.environ.get("CHNAME", "utubotss")
