import asyncio

# Recommendation: pip3 install -U tgcrypto
from pyrogram import Client

# Errors
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import UserBot
from pyrogram.errors.exceptions.bad_request_400 import UserBlocked
from pyrogram.errors.exceptions.forbidden_403 import UserPrivacyRestricted

CHAT_ID = None  # Chat ID, откуда будут браться пользователи
CHANNEL_ID = None  # Channel ID, куда будут добавляться пользователи

CheatBot = Client(
    "CheatBot",
    "api_id",  # api_id (https://my.telegram.org/app)
    "api_hash",  # api_hash (https://my.telegram.org/app)
)


async def main():
    async with CheatBot:
        async for user in CheatBot.get_chat_members(CHAT_ID):
            print(user.user.id)

            await CheatBot.send_message(
                user.user.id,
                f"CheatBot Накрутка!",
            )
            await CheatBot.add_contact(
                user.user.id,
                f"{user.user.id}",
            )
            try:
                await CheatBot.add_chat_members(
                    CHANNEL_ID,
                    user.user.id,
                )
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except UserBot:
                continue
	    except UserBlocked:
                continue
            except UserPrivacyRestricted:
            	continue


try:
    CheatBot.run(main())
except KeyboardInterrupt:
    exit()
