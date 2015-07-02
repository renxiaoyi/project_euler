import petools

primes = petools.Primes(100000)
def rad(n):
  factors, _ = petools.PrimeFactors(n, primes=primes)
  return petools.Product(factors)

maxn = 100000
radn = [rad(n) for n in range(1, maxn+1)]
getr = lambda i: radn[i-1]
ans = sorted(range(1, maxn+1), key=getr)
print ans[9999]
