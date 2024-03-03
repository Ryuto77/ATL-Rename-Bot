import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "18456806")
API_HASH = os.environ.get("API_HASH", "ffd294313d574aa52d04813ee7dedb53")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "6750339147:AAFoCm6xqXIofFnmdg7cujyUyfMMuMuEmPo")

CHANNEL = os.environ.get("CHANNEL", "") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","renext_bot")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://renext_bot:renext_bot@cluster0.y99so09.mongodb.net/")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1989750989').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001230390281"))
