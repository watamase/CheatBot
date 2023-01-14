################################################################################
## Form generated from reading UI file 'InvitationWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_InvitationWindow(object):
    def setupUi(self, InvitationWindow):
        if not InvitationWindow.objectName():
            InvitationWindow.setObjectName(u"InvitationWindow")
        InvitationWindow.resize(400, 210)
        InvitationWindow.setStyleSheet(u"QWidget {\n"
"	color: #ffffff;\n"
"	background-color: #121212;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 2px solid #ffffff;\n"
"	border-radius: 12px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 2px solid #ffffff;\n"
"	border-radius: 12px;\n"
"	font-size: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #bfbfbf;\n"
"	border: 2px solid #bfbfbf;\n"
"}")
        self.centralwidget = QWidget(InvitationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_edit_parse_from = QLineEdit(self.centralwidget)
        self.line_edit_parse_from.setObjectName(u"line_edit_parse_from")
        self.line_edit_parse_from.setGeometry(QRect(20, 20, 361, 41))
        self.line_edit_invite_to = QLineEdit(self.centralwidget)
        self.line_edit_invite_to.setObjectName(u"line_edit_invite_to")
        self.line_edit_invite_to.setGeometry(QRect(20, 80, 361, 41))
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(20, 140, 361, 51))
        InvitationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InvitationWindow)

        QMetaObject.connectSlotsByName(InvitationWindow)
    # setupUi

    def retranslateUi(self, InvitationWindow):
        InvitationWindow.setWindowTitle(QCoreApplication.translate("InvitationWindow", u"CheatBot (Invitation)", None))
        self.line_edit_parse_from.setPlaceholderText(QCoreApplication.translate("InvitationWindow", u"Parse from: Chat/Channel ID", None))
        self.line_edit_invite_to.setPlaceholderText(QCoreApplication.translate("InvitationWindow", u"Invite to: Chat/Channel ID", None))
        self.btn_start.setText(QCoreApplication.translate("InvitationWindow", u"Start", None))
    # retranslateUi

