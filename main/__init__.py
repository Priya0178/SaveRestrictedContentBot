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
SESSION = "AgEn_BAAxts59qkSHXUfYrtBkFoGKalc5W8rCGzQ7ihdzp98RuOaodwm0UrBPfqNkiNyF-E8DLICp-CS5OtWN7MmDwqCVpaGoGwCnJzWkEMghXZFHF7K1CXSoisMCLrdAvUqzv505irO8C-KlKXrxwLrjFoCAZOqNV3nFf_rC-w43hO8ZO1AE09V04rOk00C7F8Gd66cCNOaRUARAj2f2fgRO7meya9-G7DdA9DKK9z3Jpyh_E42OsCGJS8xbsqnNB6y2RaZFthBSUbwwvwptqKZKWLrtmYDVmGVaWVF3etSQEsnyftRFnJ_cEKEc5KjYYyPHJkaVIonXIUrK00t5DpNwdYOOAAAAAGVMK8DAA"
FORCESUB = "afdgeh"
AUTH = 1479074329

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
