import petools


nd = 100
ans = 0
for i in range(nd):
  inc = petools.CominationWithRepetitions(9, i+1)
  ans += inc*(nd+1-i) - 9
print ans
