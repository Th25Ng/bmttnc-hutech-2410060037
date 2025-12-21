# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caesar.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 40, 161, 51))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.txtPlain = QLabel(self.centralwidget)
        self.txtPlain.setObjectName(u"txtPlain")
        self.txtPlain.setGeometry(QRect(130, 140, 61, 16))
        self.txtKey = QLabel(self.centralwidget)
        self.txtKey.setObjectName(u"txtKey")
        self.txtKey.setGeometry(QRect(130, 230, 31, 16))
        self.txtCipher = QLabel(self.centralwidget)
        self.txtCipher.setObjectName(u"txtCipher")
        self.txtCipher.setGeometry(QRect(120, 310, 61, 16))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(270, 130, 251, 71))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(270, 280, 251, 71))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 230, 251, 21))
        self.btnEncrypt = QPushButton(self.centralwidget)
        self.btnEncrypt.setObjectName(u"btnEncrypt")
        self.btnEncrypt.setGeometry(QRect(170, 400, 75, 24))
        self.btnDecrypt = QPushButton(self.centralwidget)
        self.btnDecrypt.setObjectName(u"btnDecrypt")
        self.btnDecrypt.setGeometry(QRect(400, 400, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CAESAR CIPHER", None))
        self.txtPlain.setText(QCoreApplication.translate("MainWindow", u"Plain Text:", None))
        self.txtKey.setText(QCoreApplication.translate("MainWindow", u"Key:", None))
        self.txtCipher.setText(QCoreApplication.translate("MainWindow", u"CipherText:", None))
        self.btnEncrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.btnDecrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())