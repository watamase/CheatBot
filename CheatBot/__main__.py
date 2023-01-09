import asyncio

from CheatBot import CheatBot
from datetime import datetime

from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.errors.exceptions.forbidden_403 import UserPrivacyRestricted
from pyrogram.errors.exceptions.bad_request_400 import UserNotMutualContact
from pyrogram.errors.exceptions.bad_request_400 import UserBot
from pyrogram.errors.exceptions.bad_request_400 import PeerFlood

RED = "\u001b[31;1m"
GREEN = "\u001b[32;1m"
YELLOW = "\u001b[33;1m"
RESET = "\u001b[0m"


async def member_parsing(parse_from: int = None) -> None:
    async with CheatBot:
        async for member in CheatBot.get_chat_members(parse_from):
            time = datetime.now().strftime("%H:%M:%S")

            if member.user.is_self:
                continue

            if member.user.is_deleted:
                continue

            if member.user.is_bot:
                continue

            with open(r"member_IDs.txt", "a") as file:
                file.write(f"{member.user.id}\n")

            print(GREEN + time, RESET + f"{member.user.id} ({member.user.first_name})")


async def user_invitation(parse_from: int = None, invite_to: int = None) -> None:

    if parse_from is None and invite_to is None:
        print(RED + datetime.now().strftime("%H:%M:%S"), RESET + "Pass values to function arguments")
        return

    async with CheatBot:
        async for member in CheatBot.get_chat_members(parse_from):
            time = datetime.now().strftime("%H:%M:%S")

            try:
                await CheatBot.add_chat_members(invite_to, member.user.id)
                print(GREEN + time, RESET + f"{member.user.id} ({member.user.first_name})")
                continue

            except FloodWait as e:
                print(RED + time, RESET + "Flood wait:", YELLOW + f"{e.value}")
                await asyncio.sleep(e.value)
                continue

            except UserPrivacyRestricted:
                print(RED + time, RESET + f"{member.user.id}", YELLOW + "(Privacy restricted)")
                continue

            except UserNotMutualContact:
                print(RED + time, RESET + f"{member.user.id}", YELLOW + "(Not mutual contact)")
                continue

            except UserBot:
                print(RED + time, RESET + f"{member.user.id}", YELLOW + "(User bot)")
                continue

            except PeerFlood:
                print(RED + time, RESET + "Peer flood", YELLOW + "(Account limited)")
                break
        return

if __name__ == "__main__":
    try:
        CheatBot.run(user_invitation(None, None))  # Replace with chat/channel IDs
    except KeyboardInterrupt:
        exit()
