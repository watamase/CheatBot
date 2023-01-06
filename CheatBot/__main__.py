from CheatBot import CheatBot
from datetime import datetime

from pyrogram.errors.exceptions.bad_request_400 import UserBot
from pyrogram.errors.exceptions.forbidden_403 import UserPrivacyRestricted

RED = "\u001b[31;1m"
GREEN = "\u001b[32;1m"
YELLOW = "\u001b[33;1m"
RESET = "\u001b[0m"

CHAT_ID = None  # int
CHANNEL_ID = None  # int


async def main():
    async with CheatBot:
        async for member in CheatBot.get_chat_members(CHAT_ID):
            ctime = datetime.now().strftime("%H:%M:%S")

            print(
                GREEN + ctime,
                RESET + f"{member.user.id} ({member.user.first_name})",
            )

            try:
                await CheatBot.add_chat_members(
                    CHANNEL_ID,
                    member.user.id,
                )
            except UserBot:
                print(
                    RED + ctime,
                    RESET + f"{member.user.id}",
                    YELLOW + "(User bot)",
                )
                continue
            except UserPrivacyRestricted:
                print(
                    RED + ctime,
                    RESET + f"{member.user.id}",
                    YELLOW + "(Privacy restricted)",
                )
                continue


if __name__ == "__main__":
    try:
        CheatBot.run(main())
    except KeyboardInterrupt:
        exit()

