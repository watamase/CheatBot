import colorama

from CheatBot import CheatBot
from datetime import datetime
from colorama import Fore, Style

colorama.init(autoreset=True)


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

            with open("member_IDs.txt", "a") as file:
                file.write(f"{member.user.id}\n")

            print(
                Style.BRIGHT + Fore.GREEN + time,
                Fore.RESET + f"{member.user.id} ({member.user.first_name})",
            )
        return
