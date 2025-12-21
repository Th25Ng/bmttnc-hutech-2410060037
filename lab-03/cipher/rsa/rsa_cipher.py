import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

# Import các thư viện xử lý mã hóa RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        # Xác định đường dẫn thư mục keys
        self.keys_folder = os.path.join(os.path.dirname(__file__), "keys")
        # Tạo thư mục keys nếu chưa có để tránh lỗi khi lưu file
        if not os.path.exists(self.keys_folder):
            os.makedirs(self.keys_folder)

    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        # Lưu private key
        with open(os.path.join(self.keys_folder, "private.pem"), "wb") as f:
            f.write(private_key)
        # Lưu public key
        with open(os.path.join(self.keys_folder, "public.pem"), "wb") as f:
            f.write(public_key)
        print("Đã sinh và lưu khoá vào thư mục keys.")

    def load_keys(self):
        try:
            with open(os.path.join(self.keys_folder, "private.pem"), "rb") as f:
                private_key = f.read()
            with open(os.path.join(self.keys_folder, "public.pem"), "rb") as f:
                public_key = f.read()
            return private_key, public_key
        except FileNotFoundError:
            return None, None

    def encrypt(self, message, key):
        pub_key = RSA.import_key(key)
        cipher = PKCS1_OAEP.new(pub_key)
        encrypted = cipher.encrypt(message.encode())
        return encrypted

    def decrypt(self, ciphertext, key):
        priv_key = RSA.import_key(key)
        cipher = PKCS1_OAEP.new(priv_key)
        decrypted = cipher.decrypt(ciphertext)
        return decrypted.decode()

    def sign(self, message, private_key):
        priv_key = RSA.import_key(private_key)
        h = SHA256.new(message.encode())
        signature = pkcs1_15.new(priv_key).sign(h)
        return signature

    def verify(self, message, signature, public_key):
        pub_key = RSA.import_key(public_key)
        h = SHA256.new(message.encode())
        try:
            pkcs1_15.new(pub_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt_2.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setText(data["signature"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if (data["is_verified"]):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Fail")
                    msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())