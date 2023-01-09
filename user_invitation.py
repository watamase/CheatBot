import asyncio
import colorama

from CheatBot import CheatBot
from datetime import datetime
from colorama import Fore, Style

from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.errors.exceptions.forbidden_403 import UserPrivacyRestricted
from pyrogram.errors.exceptions.bad_request_400 import UserNotMutualContact
from pyrogram.errors.exceptions.bad_request_400 import UserBot
from pyrogram.errors.exceptions.bad_request_400 import PeerFlood

colorama.init(autoreset=True)


async def user_invitation(parse_from: int = None, invite_to: int = None) -> None:

    if parse_from is None and invite_to is None:
        print(
            Style.BRIGHT + Fore.RED + datetime.now().strftime("%H:%M:%S"),
            Fore.RESET + "Pass values to function arguments",
        )
        return

    async with CheatBot:
        async for member in CheatBot.get_chat_members(parse_from):
            time = datetime.now().strftime("%H:%M:%S")

            try:
                await CheatBot.add_chat_members(invite_to, member.user.id)
                print(
                    Style.BRIGHT + Fore.GREEN + time,
                    Fore.RESET + f"{member.user.id} ({member.user.first_name})",
                )
                continue

            except FloodWait as e:
                print(
                    Style.BRIGHT + Fore.RED + time,
                    Fore.RESET + "Flood wait:",
                    Fore.YELLOW + f"{e.value}",
                )
                await asyncio.sleep(e.value)
                continue

            except UserPrivacyRestricted:
                print(
                    Style.BRIGHT + Fore.RED + time,
                    Fore.RESET + f"{member.user.id}",
                    Fore.YELLOW + "(Privacy restricted)",
                )
                continue

            except UserNotMutualContact:
                print(
                    Style.BRIGHT + Fore.RED + time,
                    Fore.RESET + f"{member.user.id}",
                    Fore.YELLOW + "(Not mutual contact)",
                )
                continue

            except UserBot:
                print(
                    Style.BRIGHT + Fore.RED + time,
                    Fore.RESET + f"{member.user.id}",
                    Fore.YELLOW + "(User bot)",
                )
                continue

            except PeerFlood:
                print(
                    Style.BRIGHT + Fore.RED + time,
                    Fore.RESET + "Peer flood",
                    Fore.YELLOW + "(Account limited)",
                )
                break
        return
