import hashlib

from Crypto import Random
from Crypto.Cipher import AES
import base64

from settings import CRYPTO_KEY


class Crypt(object):

    def __init__(self):
        self.key = hashlib.sha256(CRYPTO_KEY.encode()).digest()

    def pad(self, s):
        s = bytes(s, encoding='utf8')
        return s + b" " * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        cipher_text = iv + cipher.encrypt(message)
        cipher_text = base64.b64encode(cipher_text)
        cipher_text = str(cipher_text, 'utf8')
        return cipher_text

    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        plain = plaintext.strip()
        plain = plain.decode('utf8')
        return plain
