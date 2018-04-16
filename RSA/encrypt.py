from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
import sys
sys.path.append("D:\\Abhijeet Python\\Locker\Project\\QR Code")
from QRCreator import create_QR,QR_Decode
from decrypt import decryption_place


def encryption_place(plain_txt):
    public_key=private_key.publickey()
    pubDash = PKCS1_OAEP.new(public_key)
    return pubDash.encrypt(plain_txt)

def key_generation():
    random_generator = Random.new().read
    return RSA.generate(1024, random_generator)

def save_Keys():
    with open("privateKey.pem", "wb") as prfile:
        prfile.write(private_key.exportKey('PEM'))

def save_cipherText():
    with open("cipher_txt.txt", "wb") as rct:
        rct.write(cipher_txt)

def QR_Code():
    img = create_QR(cipher_txt)
    img.save('Encrypted_QR.jpg')

def result():
    print(Decipher_txt)


if __name__=='__main__':
    private_key=key_generation()
    save_Keys()
    plain_txt = input("Enter the Secret Message : \n")
    cipher_txt = encryption_place(plain_txt.encode("utf-8"))
    QR_Code()
    save_cipherText()
    a=QR_Decode()
    print(a)
    Decipher_txt = decryption_place(a)
    result()
