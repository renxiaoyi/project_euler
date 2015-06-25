# Brute force. Can be more efficient.
import petools


def FindRemainder(a, n):
  m = a*a
  return (pow(a-1, n, m) + pow(a+1, n, m)) % m


primes = petools.Primes(10**6)
assert(len(primes) > 10000)
ans = 0
for i in range(len(primes)):
  if FindRemainder(primes[i], i+1) > 10**10:
    ans = i+1
    break
print ans
