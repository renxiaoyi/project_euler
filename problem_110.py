import math

import petools

threshold = 2*4000000-1
# 3**15 > 2*4000000-1, so product of 15 distinct primes is an upper bound
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ans = petools.Product(primes)


def Prod(primes, exponents):
  n = 1
  for i in range(len(exponents)):
    n *= (primes[i]**exponents[i])
  return n


def Try(array):
  """Finds [a_0 >= a1 >= ...] so that PI(2*a_i+1) >= threshold."""
  global ans
  if Prod(primes, array) > ans:
    return
  if petools.Product([2*a+1 for a in array]) >= threshold:
    ans = Prod(primes, array)
  else:
    for a in range(1, array[-1]+1):
      Try(array+[a])


maxa = int(math.log(ans, 2))
for a0 in range(1, maxa+1):
  Try([a0])
print ans
