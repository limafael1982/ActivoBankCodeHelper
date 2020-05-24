# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet


class TextDecryptor:

    def __init__(self, encrypted_bytes_to_decrypt, pass_key):
        self.text_to_decrypt = encrypted_bytes_to_decrypt
        self.pass_key = pass_key

    def get_decrypted_bytes(self):
        enci = Fernet(self.pass_key)
        return enci.decrypt(self.text_to_decrypt)

    def get_decrypted_text(self):
        return self.get_decrypted_bytes().decode('utf-8')
