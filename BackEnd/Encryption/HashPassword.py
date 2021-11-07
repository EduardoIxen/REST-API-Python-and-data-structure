import hashlib


class HashPassword:
    def __init__(self, value):
        self.value = value

    def Hash(self):
        encoded_pass = self.value.encode()
        hasher = hashlib.sha256(encoded_pass)
        hex_dig = hasher.hexdigest()
        return hex_dig
