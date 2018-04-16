from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def decryption_place(a):
    with open("privateKey.pem", "rb") as pkey:
        private_key1 = RSA.importKey(pkey.read())
    with open("cipher_txt.txt", "r") as ctxt:
        cipher_txt = ctxt.read()
    prvtDash = PKCS1_OAEP.new(private_key1)
    if(a==cipher_txt):
        return prvtDash.decrypt(a)
    else:
        print(cipher_txt)
        return "Not Got"
