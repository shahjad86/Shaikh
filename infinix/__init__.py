from telethon import TelegramClient
import logging
import time 

openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6170331217:AAGGobUTn4lXseKNyYmHRf3dX5hspN_Irqo"

bot = TelegramClient("infinixbot", api_id, api_hash
).start(bot_token = bot_token)