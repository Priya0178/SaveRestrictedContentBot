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
SESSION = "1BVtsOLoBuyiHxazDYOrtnn4RJjgxuce8uF7uY4A4HSa72gIsG8jnSnJOH12bsbd0XQQaQc_SMW4SMBC5L4ZDc5hxmKOSIYS_da1w_ehq9z6w_gzVl394nohiXdjeBQU5mLx9A2Q95_dMO4q8-ZZBVIN6R2lP5zBR_MzlSngF4zHk8DQxzHKxoiD6knBIRw0ZSPQApAIRZR81Z0u4PyidwyQIp3GYJIyFk8hq_e6o4NaoDqfbE-qkqSvwmKtVj3HMUmj4iqMGmbY8H2Z-pbzQdKA9OXPt-Huqpl6kftCad5JqyLwe_eyjbzO8RvO6qGXWpyC06Guuga3QaZ5XMWCUGbVzrAEHvN0="
FORCESUB = "afdgeh"
AUTH = 1092802988

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
