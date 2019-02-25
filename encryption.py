from cryptography.fernet import Fernet


def encryption(key, text):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(text)
    return cipher_text


def decryption(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text
