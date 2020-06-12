z = True
c = 1
while z == 1:
    x = 17*c+5
    if x % 11 == 3 and x % 5 == 2:
        z = False
    else:
        c += 1
print(x)
# because x < 935 => 935mod872 = 872 => a = 872
"""
    x = 872
    x ≡ 2 mod 5
    x ≡ 3 mod 11
    x ≡ 5 mod 17
    x ≡ a mod 935
    https://www.dcode.fr/chinese-remainder
    https://medium.com/@fangya.123/chinese-remainder-theorem-with-python-a483de81fbb8

"""