#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("23995611", default=None, cast=int)
API_HASH = config("a1b94f10b912c9d732c320f9c73d73dc", default=None)
BOT_TOKEN = config("6118506109:AAF6eNFgbtzDhOo-M8r5Ksh5vl2O7CFKPlk", default=None)
SESSION = config("BQAGJUea7xepY1GtX4HZrVoUndYe5e3AET9mlT4TnUpIkV-JQLClKANCZDnJWCgnrJPiHfqZqZDW-qvFaQ56Pca_2qds7-iSo1_lsUNU4LFJeHs4ihSupNYkRjCqDZf5re1IzH3gBd3xZAaqaABowFrA6L-RzodjuMR-ngHsQuLDCMpxC_iRAMdLHynbsF05OS4stBRtuwc-igatc5HmCN_7WlSHut0-Po-l08zJWOrcCsYpnd32fIh5np1b0yja6pVSsGK9qQOq86HFzFMVgYDbLA4maHgkOpsAAYSPXbv8RA1GuKZkNWDwNwUJqdTBgFzmIT-SQj16YdHjJFFHsp7JAAAAAU-uEBwA", default=None)
FORCESUB = config("jammesupdates", default=None)
AUTH = config("5631774748", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

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
