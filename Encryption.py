from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP 

class EncryptionSystem:
    def __init__(self):
       pass

    def get_private_key(self):
        pass

    def get_pub_key(self):
        pass

    def gen_key(self):
        key = RSA.generate(2048)
        public_key_str = key.publickey().export_key().decode()
        private_key_str = key.export_key().decode()
        print(public_key_str)
        print()
        print(private_key_str)

    def decrypt(self, data:bytes):
        return data
        key = RSA.import_key(self.get_private_key())
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(data)

    def encrypt(self, data:bytes):
        return data
        key = RSA.import_key(self.get_pub_key())
        cipher = PKCS1_OAEP.new(key)
        return cipher.encrypt(data)
