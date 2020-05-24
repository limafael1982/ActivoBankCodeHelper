# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet


class TextEncryptor:

    def __init__(self, text_to_encrypt, pass_key=Fernet.generate_key()):
        self.text_to_encrypt = text_to_encrypt
        self.pass_key = pass_key

    def get_encrypted_text(self):
        enci = Fernet(self.pass_key)
        return enci.encrypt(bytes(self.text_to_encrypt, encoding='utf-8'))

    def get_generated_key(self):
        return str(self.pass_key)
