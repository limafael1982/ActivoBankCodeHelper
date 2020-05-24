# -*- coding: utf-8 -*-

import unittest
from cryptography.fernet import Fernet
from aux_classes.TextDecryptor import TextDecryptor
from aux_classes.TextEncryptor import TextEncryptor


class EncryptDecryptTests(unittest.TestCase):
    def test_should_encrypt_and_decrypt_properly(self):
        key = Fernet.generate_key()
        expected_text = 'This text should be encrypted and decrypted'
        text_enc_obj = TextEncryptor(text_to_encrypt=expected_text, pass_key=key)
        enc_text = text_enc_obj.get_encrypted_text()
        text_dec_obj = TextDecryptor(encrypted_bytes_to_decrypt=enc_text, pass_key=key)
        decrypted_text = text_dec_obj.get_decrypted_text()
        self.assertEqual(expected_text, decrypted_text)
