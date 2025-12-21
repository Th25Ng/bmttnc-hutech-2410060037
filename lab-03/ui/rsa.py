# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rsa.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 550)
        # Áp dụng Font chữ hệ thống hiện đại
        font_main = QtGui.QFont("Segoe UI", 10)
        MainWindow.setFont(font_main)
        
        # Style chung cho toàn bộ ứng dụng
        MainWindow.setStyleSheet("""
            QMainWindow { background-color: #f0f2f5; }
            QLabel { color: #333; font-weight: bold; }
            QTextEdit { 
                background-color: white; 
                border: 1px solid #dcdfe6; 
                border-radius: 5px; 
                padding: 5px; 
            }
            QPushButton {
                background-color: #409eff;
                color: white;
                border-radius: 4px;
                padding: 5px 15px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover { background-color: #66b1ff; }
            QPushButton:pressed { background-color: #3a8ee6; }
            #btn_gen_keys { background-color: #67c23a; }
            #btn_gen_keys:hover { background-color: #85ce61; }
            #label_title { color: #2c3e50; margin-bottom: 20px; }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Tiêu đề chính
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 750, 50))
        font_title = QtGui.QFont("Segoe UI", 24, QtGui.QFont.Bold)
        self.label.setFont(font_title)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label_title")

        # Nút Generate Keys (để góc trên bên phải cho gọn)
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(560, 30, 131, 35))
        self.btn_gen_keys.setObjectName("btn_gen_keys")

        # --- Cột trái: Encryption/Decryption ---
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 150, 20))
        self.label_2.setObjectName("label_2")
        
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(40, 115, 310, 100))
        self.txt_plain_text.setObjectName("txt_plain_text")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 150, 20))
        self.label_4.setObjectName("label_4")

        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(40, 255, 310, 100))
        self.txt_cipher_text.setObjectName("txt_cipher_text")

        self.btn_encrypt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt_2.setGeometry(QtCore.QRect(40, 370, 145, 40))
        self.btn_encrypt_2.setObjectName("btn_encrypt_2")

        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(205, 370, 145, 40))
        self.btn_decrypt.setObjectName("btn_decrypt")

        # --- Cột phải: Digital Signature ---
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 90, 150, 20))
        self.label_3.setObjectName("label_3")

        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(400, 115, 310, 100))
        self.txt_info.setObjectName("txt_info")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 230, 150, 20))
        self.label_5.setObjectName("label_5")

        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(400, 255, 310, 100))
        self.txt_sign.setObjectName("txt_sign")

        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(400, 370, 145, 40))
        self.btn_sign.setObjectName("btn_sign")

        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(565, 370, 145, 40))
        self.btn_verify.setObjectName("btn_verify")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Encryption Tool"))
        self.label.setText(_translate("MainWindow", "RSA CRYPTOSYSTEM"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.label_2.setText(_translate("MainWindow", "Plain Text"))
        self.label_4.setText(_translate("MainWindow", "Cipher Text"))
        self.btn_encrypt_2.setText(_translate("MainWindow", "ENCRYPT"))
        self.btn_decrypt.setText(_translate("MainWindow", "DECRYPT"))
        self.label_3.setText(_translate("MainWindow", "Message Content"))
        self.label_5.setText(_translate("MainWindow", "Signature"))
        self.btn_sign.setText(_translate("MainWindow", "SIGN"))
        self.btn_verify.setText(_translate("MainWindow", "VERIFY"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())