import itertools
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


def _TestPrimes():
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  for i in range(50):
    actual = Primes(i)
    expected = [x for x in primes if x <= i]
    assert actual == expected


def IsPrime(num, primes=None):
  if num <= 1:
    return False
  sq = int(math.sqrt(num)) + 1
  if not primes:
    i = 2
    while i < sq:
      if num%i == 0:
        return False
      i += 1
    return True
  else:
    for p in primes:  # primes should be sorted
      if p >= sq:
        return True
      if num%p == 0:
        return False
    return True


def _TestIsPrime():
  max_num = 1000
  primes = Primes(max_num)
  for n in range(max_num):
    a, b, c = IsPrime(n), IsPrime(n, primes), (n in primes)
    assert a == b == c


def PrimeFactors(num, primes=None):
  """Returns prime factors and their exponents of the given number."""
  assert num > 0
  if not primes:
    primes = Primes(num)
  factors, exponents = [], []
  for p in primes:
    exp = 0
    while num != 1 and num % p == 0:
      num /= p
      exp += 1
    if exp > 0:
      factors.append(p)
      exponents.append(exp)
    if num == 1:
      break
  return factors, exponents


def _TestPrimeFactors():
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


def _TestProducts():
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


def DivisorsInter(factors, exponents):
  """Returns a list of all divisors of the given number (factors, exponents)."""
  exp_tuples = [range(e+1) for e in exponents]
  divisors = []
  for exp in itertools.product(*exp_tuples):
    fe = [factors[i]**exp[i] for i in range(len(exp))]
    divisors.append(Product(fe))
  divisors.sort()
  return divisors


def Divisors(num, primes=None):
  """Returns a list of all divisors of the given number."""
  factors, exponents = PrimeFactors(num, primes)
  return DivisorsInter(factors, exponents)


def _TestDivisors():
  actual = Divisors(1)
  expected = [1]
  assert actual == expected
  actual = Divisors(2)
  expected = [1, 2]
  assert actual == expected
  actual = Divisors(28)
  expected = [1, 2, 4, 7, 14, 28]
  assert actual == expected
  actual = Divisors(16)
  expected = [1, 2, 4, 8, 16]
  assert actual == expected
  actual = Divisors(108)
  expected = [1, 2, 3, 4, 6, 9, 12, 18, 27, 36, 54, 108]
  assert actual == expected


def GenComposites(primes, max_num):
  """Generates composites (<= 'max_num') using input 'primes' set."""
  def Try(factors):
    num = Product(factors)
    if len(factors) >= 2 and num <= max_num:
      yield num, factors
    for p in primes:  # primes are sorted
      if num*p > max_num:
        break
      if len(factors) == 0 or p >= factors[-1]:
        for n, f in Try(factors+[p]):
          yield n, f
  return Try([])


def _TestGenComposites():
  actual = [''.join(map(str, f)) for n,f in GenComposites([2,3,5], 20)]
  expected = ['22', '222', '2222', '223', '225', '23', '233', '25', '33', '35']
  assert actual == expected
  max_num = 10000
  primes = Primes(max_num)
  composites = [n for n, f in GenComposites(primes, max_num)]
  assert len(composites) == len(set(composites))
  assert len(primes) + len(composites) == max_num - 1


def Group(array):
  """Groups duplicate elements, e.g. [2, 1, 2, 2, 3] => [1, 2, 3], [1, 3, 1]."""
  array.sort()
  uniq, cnts = [], []
  for i in array:
    if len(uniq) == 0 or i != uniq[-1]:
      uniq.append(i)
      cnts.append(1)
    else:
      cnts[-1] += 1
  return uniq, cnts


def _TestGroup():
  actual1, actual2 = Group([2, 1, 2, 2, 3])
  expected1, expected2 = [1, 2, 3], [1, 3, 1]
  assert actual1 == expected1
  assert actual2 == expected2


def SumOfDivisors(num, primes=None):
  """Sum of positive divisors."""
  factors, exponents = PrimeFactors(num, primes)
  # http://en.wikipedia.org/wiki/Divisor_function.
  sigma = 1
  for i in range(len(factors)):
    p, a = factors[i], exponents[i]
    s = sum([p**e for e in range(a+1)])
    sigma *= s
  return sigma


def _TestSumOfDivisors():
  for i in range(1, 100):
    expected = sum(Divisors(i))
    actual = SumOfDivisors(i)
    assert expected == actual


def Flatten(matrix):
  """Flattens a 2d array 'matrix' to an array."""
  array = []
  for a in matrix:
    array += a
  return array


def MulMod(a, b, m):
  if a >= m:
    a %= m
  if b >= m:
    b %= m
  return a*b%m


def PowMod(a, e, m):
  """Deprecated. Use pow(a, e, m) instead."""
  if e == 0:
    return 1%m
  if e == 1:
    return a%m
  return MulMod(PowMod(a, e/2, m), PowMod(a, e-e/2, m), m)


def _TestPowMod():
  for e in range(20):
    assert 2**e%11 == PowMod(2, e, 11)
    assert 3**e%11 == PowMod(3, e, 11)


def Permutations(seq):
  """Yield only unique permutations of seq in an efficient way.

  http://stackoverflow.com/questions/12836385
  """
  # Precalculate the indices we'll be iterating over for speed
  i_indices = range(len(seq) - 1, -1, -1)
  k_indices = i_indices[1:]

  # The algorithm specifies to start with a sorted version
  seq = sorted(seq)

  while True:
    yield seq

    # Working backwards from the last-but-one index,           k
    # we find the index of the first decrease in value.  0 0 1 0 1 1 1 0
    for k in k_indices:
      if seq[k] < seq[k + 1]:
        break
    else:
      # Introducing the slightly unknown python for-else syntax:
      # else is executed only if the break statement was never reached.
      # If this is the case, seq is weakly decreasing, and we're done.
      return

    # Get item from sequence only once, for speed
    k_val = seq[k]

    # Working backwards starting with the last item,           k     i
    # find the first one greater than the one at k       0 0 1 0 1 1 1 0
    for i in i_indices:
      if k_val < seq[i]:
        break

    # Swap them in the most efficient way
    (seq[k], seq[i]) = (seq[i], seq[k])                #       k     i
                                                       # 0 0 1 1 1 1 0 0

    # Reverse the part after but not                           k
    # including k, also efficiently.                     0 0 1 1 0 0 1 1
    seq[k + 1:] = seq[-1:k:-1]


def _TestPermutations():
  perm = set([','.join(p) for p in Permutations(['1', '2', '1'])])
  assert perm == set(['1,1,2', '1,2,1', '2,1,1'])


class Memorize(object):
  def __init__(self, f):
    self.func = f
    self.memo = {}

  def __call__(self, *args):
    if not args in self.memo:
      self.memo[args] = self.func(*args)
    return self.memo[args]


def IsPalindrome(s):
  return s == s[::-1]


if __name__ == '__main__':
  _TestPrimes()
  _TestIsPrime()
  _TestPrimeFactors()
  _TestProducts()
  _TestDivisors()
  _TestGenComposites()
  _TestGroup()
  _TestSumOfDivisors()
  _TestPowMod()
  _TestPermutations()
  print 'pass'
