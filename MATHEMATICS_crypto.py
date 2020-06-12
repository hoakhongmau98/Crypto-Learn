

# Modular Inverting
# g * d = x mod p
def modular_inverting(g, x, p):
    i = 1
    n = True
    while n == 1:
        z = (p * i) + x
        if (z % g) == 0:
            n = False
        else:
            i += 1
    return f'd = {z/g}'
    
    
print(modular_inverting(4, 1, 13))
