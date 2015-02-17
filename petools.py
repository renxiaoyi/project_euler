import math


def Primes(max_num):
  """Returns all primes <= 'max_num'."""
  is_prime = [True]*(max_num+1)
  is_prime[0] = False
  if max_num > 0: is_prime[1] = False
  for i in [x for x in range(int(math.sqrt(max_num))+1) if x > 1]:
    f = 2
    while i*f <= max_num:
      is_prime[i*f] = False
      f += 1
  return [x for x in range(max_num+1) if is_prime[x]]


def TestPrimes():
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  for i in range(50):
    actual = Primes(i)
    expected = [x for x in primes if x <= i]
    assert actual == expected


def PrimeFactors(num):
  """Returns prime factors and their exponents of the given number."""
  factors, exponents = [], []
  primes = Primes(num)
  for p in primes:
    exp = 0
    while num % p == 0 and num != 0:
      num /= p
      exp += 1
    if exp > 0:
      factors.append(p)
      exponents.append(exp)
    if num == 0:
      break
  return factors, exponents


def TestPrimeFactors():
  actual1, actual2 = PrimeFactors(1)
  expected1, expected2 = [], []
  assert actual1 == expected1, actual2 == expected2
  actual1, actual2 = PrimeFactors(2)
  expected1, expected2 = [2], [1]
  assert actual1 == expected1, actual2 == expected2
  actual1, actual2 = PrimeFactors(42)
  expected1, expected2 = [2, 3, 7], [1, 1, 1]
  assert actual1 == expected1, actual2 == expected2
  actual1, actual2 = PrimeFactors(99)
  expected1, expected2 = [3, 11], [2, 1]
  assert actual1 == expected1, actual2 == expected2


def Products(num, min_divisor=2):
  """Naive method to generate all expressions of 'num' as a product of ints."""
  if num == 1:
    yield []
  for divisor in range(min_divisor, num+1):
    if num % divisor == 0:
      for partial in Products(num/divisor, divisor):
        yield partial + [divisor]


def TestProducts():
  actual = []
  for product in Products(24):
    actual.append('*'.join(map(str, product)))
  expected = ['3*2*2*2', '6*2*2', '4*3*2', '12*2', '8*3', '6*4', '24']
  assert actual == expected


def Combination(n, k):
  return math.factorial(n) / math.factorial(k) / math.factorial(n-k)


def CominationWithRepetitions(n, k):
  return Combination(n+k-1, k)


def Product(iterable):
  p = 1
  for n in iterable:
    p *= n
  return p


def Area(a, b, c):
  """Heron's formula."""
  p = (a+b+c)/2
  return math.sqrt(p*(p-a)*(p-b)*(p-c))


if __name__ == '__main__':
  TestPrimes()
  TestPrimeFactors()
  TestProducts()
  print 'pass'
