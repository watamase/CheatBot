import os
import argparse
import colorama

from CheatBot import CheatBot
from datetime import datetime
from colorama import Fore, Style

from member_parsing import member_parsing
from user_invitation import user_invitation

colorama.init(autoreset=True)


def clear_console() -> None:
    command = "clear"

    if os.name in ("nt", "dos"):
        command = "cls"

    os.system(command)


def main(use_member_parsing: bool = False, use_user_invitation: bool = False) -> None:
    if (use_member_parsing and use_user_invitation) or (not use_member_parsing and not use_user_invitation):
        print(
            Style.BRIGHT + Fore.RED + datetime.now().strftime("%H:%M:%S"),
            Fore.RESET + "Two arguments cannot have the same value",
        )

    if use_member_parsing:
        try:
            parse_from = int(input("Parse from (ID): "))
        except ValueError:
            print(
                Style.BRIGHT + Fore.RED + datetime.now().strftime("%H:%M:%S"),
                Fore.RESET + "Value error",
            )
            exit()
        except KeyboardInterrupt:
            clear_console()
            exit()

        clear_console()
        CheatBot.run(member_parsing(parse_from))

    if use_user_invitation:
        try:
            parse_from = int(input("Parse from (ID): "))
            invite_to = int(input("Invite to (ID): "))
        except ValueError:
            print(
                Style.BRIGHT + Fore.RED + datetime.now().strftime("%H:%M:%S"),
                Fore.RESET + "Value error",
            )
            exit()
        except KeyboardInterrupt:
            clear_console()
            exit()

        clear_console()
        CheatBot.run(user_invitation(parse_from, invite_to))


parser = argparse.ArgumentParser()
parser.add_argument(
    "--member_parsing",
    help="Iterating over member IDs and writing them to a file (Bool) [True/False]",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--user_invitation",
    help="Invite users to chat/channel (Bool) [True/False]",
    action="store_true",
    default=False,
)

args = parser.parse_args()

if __name__ == "__main__":
    main(args.member_parsing, args.user_invitation)
