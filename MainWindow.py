################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: #ffffff;\n"
"	background-color: #121212;\n"
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
"}\n"
"\n"
"QLabel {\n"
"	font-size: 48px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(8, 5, 381, 81))
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_parsing = QPushButton(self.centralwidget)
        self.btn_parsing.setObjectName(u"btn_parsing")
        self.btn_parsing.setGeometry(QRect(70, 100, 261, 51))
        self.btn_invitation = QPushButton(self.centralwidget)
        self.btn_invitation.setObjectName(u"btn_invitation")
        self.btn_invitation.setGeometry(QRect(70, 170, 261, 51))
        self.btn_spam = QPushButton(self.centralwidget)
        self.btn_spam.setObjectName(u"btn_spam")
        self.btn_spam.setGeometry(QRect(70, 240, 261, 51))
        self.btn_about = QPushButton(self.centralwidget)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setGeometry(QRect(70, 310, 261, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CheatBot", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"</>", None))
        self.btn_parsing.setText(QCoreApplication.translate("MainWindow", u"Parsing", None))
        self.btn_invitation.setText(QCoreApplication.translate("MainWindow", u"Invitation", None))
        self.btn_spam.setText(QCoreApplication.translate("MainWindow", u"Spam", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

