from cryptography.fernet import Fernet


class Encryption:
    def __init__(self) -> None:
        pass

    def encrypt(self, key, data):
        f  = Fernet(key)
        enctipted = f.encrypt(data.encode())
        return enctipted

    def decrypt(self, key, data):
        f2 = Fernet(key)
        decrypted = f2.decrypt(data)
        return decrypted

