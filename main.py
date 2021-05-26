from telethon.sync import TelegramClient, events, Button
from telethon import errors
from telethon.tl.types import InputPeerChat
from telethon.errors import FloodWaitError
from telethon.tl.types import ChatEmpty
import os
import uuid
import shutil
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from creds import Credentials

client = TelegramClient('Telethon Anonymous Bot',
                    api_id = Credentials.API_ID,
                    api_hash=Credentials.API_HASH).start(bot_token=Credentials.BOT_TOKEN)

DEFAULT_START = ("👋 Hey!I am ANONYMOUS SENDER BOT.\n\n"
                 "✅ Just Forward me some messages or media and I will anonymize the sender✅.\n\n"
                 "👨‍💻 Please support the developer by subscribe his  channel 🔥 https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA 🔥 .")


if Credentials.START_MESSAGE is not None:
  START_TEXT = Credentials.START_MESSAGE
else:
  START_TEXT = DEFAULT_START
  
@client.on(events.NewMessage)
async def startmessage(event):
  try:
    if '/start' in event.raw_text:
      ok = event.chat_id
      await client.send_message(event.chat_id,
                                message=START_TEXT,
                                buttons=[[Button.url("📦socure code 📦","https://github.com/supunmadurangasl/Anonymous-bot"),
                                         Button.url("👨‍💻Support Channel👨‍💻","https://t.me/FreeNetSL")]])                                                                
    if event.message.media:
      await client.send_message(event.chat_id,file=event.message.media)
    else:
      await client.send_message(event.chat_id,event.message)
  except FloodWaitError as e:
    pass
    

with client:
  client.run_until_disconnected() 
