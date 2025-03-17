from flask import Flask, request, jsonify  # Added necessary imports
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Caesar Cipher Algorithm
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])  # Fixed parentheses issue
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})  # Corrected jsonify return type

@app.route("/api/caesar/decrypt", methods=["POST"])  # Fixed parentheses issue
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})  # Corrected jsonify return type

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
