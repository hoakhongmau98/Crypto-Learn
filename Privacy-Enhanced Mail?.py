from Crypto.PublicKey import RSA
import base64
# make_key form test number (2048)
# key = RSA.generate(2048)
# f = open('mykey.pem', 'wb')
# f.write(key.export_key('PEM'))
# f.close()

f = open('keypair_1f696c053d76a78c2c531bb013a92d4a.pem', 'r')
key = RSA.import_key(f.read())

"""
https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-1/
Variables:
n (integer) – RSA modulus
e (integer) – RSA public exponent
d (integer) – RSA private exponent
p (integer) – First factor of the RSA modulus
q (integer) – Second factor of the RSA modulus
u – Chinese remainder component (p−1mod q)
"""
print(f"d:\n{key.d}")
print(f"n:\n{key.n}")
print(f"e:\n{key.e}")
print(f"p:\n{key.p}")
print(f"q:\n{key.q}")
print(f"u:\n{key.u}")
