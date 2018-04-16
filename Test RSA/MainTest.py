from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
privateKey_gen=RSA.generate(1024,random_generator)
p_key=privateKey_gen.publickey()#testing purpose

print(privateKey_gen.exportKey(format='PEM',pkcs=8))

#encryption
f=open('private.pem','wb')
f.write(privateKey_gen.exportKey('PEM'))
f.close()

f = open('private.pem','rb')
newkey = RSA.importKey(f.read())#private key
public_key=newkey.publickey()

if(p_key==public_key):

    c_key=PKCS1_OAEP.new(public_key) #cipher key msg=newkey.enc

    chipher_txt=c_key.encrypt(b'abhijeet')
    print(chipher_txt)
    print("abhijeet")

#decrypt
fD=open('private.pem','rb')
decipher_key=RSA.importKey(fD.read())
if(decipher_key==privateKey_gen):
    dcipherKey=PKCS1_OAEP.new(decipher_key)
    pt=dcipherKey.decrypt(chipher_txt)
    print(pt)