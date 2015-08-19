import petools

# # Works, but slow.
# def LeastN1(p1, p2):
#   r = p2 - p1
#   n = 10
#   while n < p1:
#     n *= 10
#   rem = n % p2
#   k = 0
#   while (k*p2 + r) % rem != 0:
#     k += 1
#   return (k*p2 + r)/rem*n + p1

def LeastN(p1, p2):
  d = 10
  while d < p1:
    d *= 10
  # d*k + p1 == 0 (mod p2), so k == (p2-p1)*x (mod p2) if k is not prime, where
  # x = d^(-1) is the modular inverse of d (mod p2), i.e. x*d - y*p2 = 1.
  x, y, c = petools.ExtendedGcd(d, p2)
  while x < 0:
    x += p2
  k = (p2-p1)*x
  while k > p2:
    k -= p2
  return d*k+p1

maxp1 = 10**6
primes = petools.Primes(2*maxp1)
ans = 0
for i in range(len(primes)):
  if i < 3:
    continue
  p1, p2 = primes[i-1], primes[i]
  if p1 > maxp1:
    break
  ans += LeastN(p1, p2)
print ans

# 18613426663617118
