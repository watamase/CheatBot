################################################################################
## Form generated from reading UI file 'SpamWindow.ui'
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

class Ui_SpamWindow(object):
    def setupUi(self, SpamWindow):
        if not SpamWindow.objectName():
            SpamWindow.setObjectName(u"SpamWindow")
        SpamWindow.resize(400, 211)
        SpamWindow.setStyleSheet(u"QWidget {\n"
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
        self.centralwidget = QWidget(SpamWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_edit_spam_to = QLineEdit(self.centralwidget)
        self.line_edit_spam_to.setObjectName(u"line_edit_spam_to")
        self.line_edit_spam_to.setGeometry(QRect(20, 20, 361, 41))
        self.line_edit_text = QLineEdit(self.centralwidget)
        self.line_edit_text.setObjectName(u"line_edit_text")
        self.line_edit_text.setGeometry(QRect(20, 80, 311, 41))
        self.btn_select_text_file = QPushButton(self.centralwidget)
        self.btn_select_text_file.setObjectName(u"btn_select_text_file")
        self.btn_select_text_file.setGeometry(QRect(340, 80, 41, 41))
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(20, 140, 360, 51))
        SpamWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpamWindow)

        QMetaObject.connectSlotsByName(SpamWindow)
    # setupUi

    def retranslateUi(self, SpamWindow):
        SpamWindow.setWindowTitle(QCoreApplication.translate("SpamWindow", u"CheatBot (Spam)", None))
        self.line_edit_spam_to.setPlaceholderText(QCoreApplication.translate("SpamWindow", u"Spam to: Chat/User ID", None))
        self.line_edit_text.setPlaceholderText(QCoreApplication.translate("SpamWindow", u"Text", None))
        self.btn_select_text_file.setText(QCoreApplication.translate("SpamWindow", u"...", None))
        self.btn_start.setText(QCoreApplication.translate("SpamWindow", u"Start", None))
    # retranslateUi

