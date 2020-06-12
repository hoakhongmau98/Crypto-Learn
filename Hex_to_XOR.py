# decode tex form hex
decoded = bytearray.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d').decode()
# decoded = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104').decode('utf-8')
# 1 byte = 8bit = 256
for i in range(0, 255):
    res = []
    for letter in decoded:
        res.append(chr(ord(letter) ^ i))
    if 'crypto' in ''.join(res):
        print(''.join(res))
