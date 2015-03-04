import petools

primes = petools.Primes(10000)


def NumOfSolutions(n):
  _, exp = petools.PrimeFactors(n, primes)
  n2_factors = petools.Product([2*e+1 for e in exp])
  return (n2_factors+1)/2


ans = 1000
while True:
  if NumOfSolutions(ans) > 1000:
    break
  ans += 1
print ans
