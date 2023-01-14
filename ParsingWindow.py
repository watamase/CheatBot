################################################################################
## Form generated from reading UI file 'ParsingWindow.ui'
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

class Ui_ParsingWindow(object):
    def setupUi(self, ParsingWindow):
        if not ParsingWindow.objectName():
            ParsingWindow.setObjectName(u"ParsingWindow")
        ParsingWindow.resize(400, 150)
        ParsingWindow.setStyleSheet(u"QWidget {\n"
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
        self.centralwidget = QWidget(ParsingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_edit_id = QLineEdit(self.centralwidget)
        self.line_edit_id.setObjectName(u"line_edit_id")
        self.line_edit_id.setGeometry(QRect(20, 20, 361, 41))
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(20, 80, 361, 51))
        ParsingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ParsingWindow)

        QMetaObject.connectSlotsByName(ParsingWindow)
    # setupUi

    def retranslateUi(self, ParsingWindow):
        ParsingWindow.setWindowTitle(QCoreApplication.translate("ParsingWindow", u"CheatBot (Parsing)", None))
        self.line_edit_id.setPlaceholderText(QCoreApplication.translate("ParsingWindow", u"Chat/Channel ID", None))
        self.btn_start.setText(QCoreApplication.translate("ParsingWindow", u"Start", None))
    # retranslateUi

