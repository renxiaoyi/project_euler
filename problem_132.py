import petools

def LeastN(m):
  # Returns the least n so that m divides R(n).
  assert m % 2 != 0
  assert m % 5 != 0
  r = 1  # remainder 10^(n-1) % m
  rem = 1 # remainder R(n) % m
  n = 2
  while True:
    r = 10*r % m
    rem = (rem+r) % m
    if rem == 0:
      return n
    n += 1

primes = petools.Primes(10**6)
ans = 0
cnt = 0
for p in primes:
  if p < 7:
    continue
  if 10**9 % LeastN(p) == 0:
    ans += p
    cnt += 1
    print cnt, p
    if cnt == 40:
      break
print ans
