#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 19397648
API_HASH = "ed2db4aa6ab5f67fde7b88b8f17e85d0"
BOT_TOKEN = "6055215937:AAFXHPlvJxpMqlEsIKauVS71SlSRy8DT1GM"
SESSION = "BQEn_BAAkmGhqAbfVe_R-zsT9YJMEmNkP9I-9ItzxyDNpyqZBWK6-y3d7zBtQ-Q59LToytsMMAgD7PRBEDmoLXLz_W5pGWxKuzORlxcUxgdXp_FeRZ6oDnIrNeKgjtU5mQ4qHofEhURC2Mz1pr7dYAS45WXTf7QORg2yWPzUnIfNMVuzxcHwPcnWJUhDnD8kNyocLkf2fqQ3U1wajufCwCe6gp_3FFnWb-435wvAMqXUP3JFYzd1x3uFyTLx1qgl3McTAcgFT_n_CsrRieumQSs3reknyj7V-LvyTVm9fH9rq82xx4bheMZwh7IUYB90RNxj9XSR5TZgae_hEDJUFFrErbzLFwAAAAFlo69vAA"
FORCESUB = ""
AUTH = ""

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
