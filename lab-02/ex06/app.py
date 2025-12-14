from flask import Flask, render_template, request, json
from ex01.cipher.caesar import CaesarCipher
from ex04.cipher.playfair.playfair_cipher import PlayFairCipher

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#router routes for playfair cypher
# Route để hiển thị trang Playfair
@app.route("/playfair")
def playfair_page():
    return render_template('playfair.html')

# Route để xử lý cả mã hóa và giải mã
@app.route("/playfair/process", methods=['POST'])
def playfair_process():
    # Kiểm tra xem module playfair đã được import thành công chưa
    if not PlayFairCipher:
        return "Error: Playfair cipher logic is not available. Check server logs for import errors."

    # Lấy dữ liệu chung từ form
    text = request.form['inputText']
    key = request.form['inputKey']
    action = request.form['action'] # Lấy giá trị của nút được nhấn ('Encrypt' hoặc 'Decrypt')

    result = ""
    result_label = ""
    
    playfair = PlayFairCipher()

    playfair_matrix = playfair.create_playfair_matrix(key)

    if action == 'Encrypt':
        result = playfair.playfair_encrypt(text, playfair_matrix)
        result_label = "Encrypted Text"
    elif action == 'Decrypt':
        result = playfair.playfair_decrypt(text, playfair_matrix)
        result_label = "Decrypted Text"

    # Trả về lại trang playfair.html với các giá trị đã tính toán
    return render_template('playfair.html', 
                           result=result,
                           result_label=result_label,
                           text_input=text,
                           key_input=key)

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)