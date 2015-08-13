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

def Check25(n):
  while n > 1:
    if n % 2 == 0:
      n /= 2
    elif n % 5 == 0:
      n /= 5
    else:
      return False
  return n == 1

primes = petools.Primes(10**5)
ans = 2 + 3 + 5
for p in primes:
  if p < 7:
    continue
  if Check25(LeastN(p)):
    print p
  else:
    ans += p
print ans
