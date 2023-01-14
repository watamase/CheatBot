import sys

from PySide6.QtWidgets import QApplication

from CheatBot_gui import (
    CheatBotMainGUI,
    CheatBotParsingGUI,
    CheatBotInvitation,
    CheatBotSpam,
)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = CheatBotMainGUI()
    main_window.show()

    parsing_window = CheatBotParsingGUI()
    parsing_window.show()

    invitation_window = CheatBotInvitation()
    invitation_window.show()

    spam_window = CheatBotSpam()
    spam_window.show()

    sys.exit(app.exec())
