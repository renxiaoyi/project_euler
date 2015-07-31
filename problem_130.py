import petools

def A(n):
  # Returns the least k so that n divides R(k).
  if n % 2 == 0 or n % 5 == 0:
    return 0
  if n == 1:
    return 1
  r = 1  # remainder 10^(k-1) % n
  rem = 1 # remainder R(k) % n
  k = 1
  while True:
    k += 1
    r = 10*r % n
    rem = (rem+r) % n
    if rem == 0:
      return k

max_n = 10**6
primes = petools.Primes(max_n)
wanted = []
for n in xrange(3, max_n+1, 2):
  if n % 5 == 0 or n in primes:
    continue
  if (n-1) % A(n) == 0:
    wanted.append(n)
    print n
  if len(wanted) == 25:
    break
print sum(wanted)
