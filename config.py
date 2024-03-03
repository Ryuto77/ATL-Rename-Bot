import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "18456806")
API_HASH = os.environ.get("API_HASH", "ffd294313d574aa52d04813ee7dedb53")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "6750339147:AAFoCm6xqXIofFnmdg7cujyUyfMMuMuEmPo")

CHANNEL = os.environ.get("CHANNEL", "") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","renext_bot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","AniDiscuz") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","Manga_Valley") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","Ryuto77")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","renext_bot")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://renext_bot:renext_bot@cluster7.v4tgq6h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster7")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1624191616').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001504426044"))
