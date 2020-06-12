import Crypto
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes
import codecs
import base64
from sys import argv
str_out = {}
len_argv = int(len(argv[4]))
# nc socket.cryptohack.org 13377
# connect by teminal and
if len_argv < 6:
    z = []
    z.append(int(argv[4][1:-1]))
    [z.append(int(x[:-1])) for x in argv[5:-1]]
    z.append(int(argv[-1][:-2]))
    str_in = {argv[1][1:-1]: argv[2][:-1], argv[3][:-1]: z}
    print('here')
else:
    print('not here')
    str_in = {argv[1][1:-1]: argv[2][:-1], argv[3][:-1]: str(argv[4][:-1])}
print(str_in)
print(type(str_in))
if str_in['type'] == "base64":
    # {"type": "base64", "encoded": "cmVwcm9vZmluZ19sZXZpZXNfbWVtb2lycw=="}
    encoded = base64.b64decode(str_in['encoded'])  # wow so encode
    encoded = str(encoded)
    encoded = encoded[2:-1]
elif str_in['type'] == "hex":
    # {"type": "hex", "encoded": "6162757a7a5f73796e746865746963616c6c795f4a6172726f6473"}
    encoded = bytes.fromhex(str_in['encoded']).decode('utf-8')
elif str_in['type'] == "rot13":
    # {"type": "rot13", "encoded": "pbzchgngvbaf_oyvax_snzvyvnevgl"}
    encoded = codecs.encode(str_in['encoded'], 'rot_13')
elif str_in['type'] == "bigint":
    # {"type": "bigint", "encoded": "0x726f645f73636f6e63655f48696d616c617961"}
    str_hex = str_in['encoded']
    str_hex = str_hex[2:]
    encoded = bytes.fromhex(str_hex).decode('utf-8')
    # encoded = long_to_bytes(encoded)
elif str_in['type'] == "utf-8":
    # {"type": "utf-8", "encoded": [109, 105, 110, 117, 116, 105, 97, 95, 84, 114, 101,
    # 107, 107, 105, 101, 95, 99, 111, 117, 110, 116, 97, 98, 108, 101]}
    encoded = ''
    for b in str_in['encoded']:
        encoded = encoded + chr(b)
str_out["decoded"] = encoded
print('{'+f'"decoded": "{encoded}"'+'}')



