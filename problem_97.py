import petools


m = 10**10
a = 28433
b = petools.PowMod(2, 7830457, m)
print (petools.MulMod(a, b, m) + 1) % m
