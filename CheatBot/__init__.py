from config import API
from pyrogram import Client

CheatBot = Client(
    name="CheatBot",
    api_id=API["API_ID"],
    api_hash=API["API_HASH"],
)
