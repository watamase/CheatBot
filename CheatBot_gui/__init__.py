from PySide6.QtWidgets import QMainWindow

from MainWindow import Ui_MainWindow
from ParsingWindow import Ui_ParsingWindow
from InvitationWindow import Ui_InvitationWindow


class CheatBotMainGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class CheatBotParsingGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ParsingWindow()
        self.ui.setupUi(self)


class CheatBotInvitation(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_InvitationWindow()
        self.ui.setupUi(self)
