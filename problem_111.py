import itertools

import petools


def Dig2Num(digits):
  num = 0
  for d in digits:
    num = num*10+d
  return num


def GenNums(n, m, d):
  """Generates 'n'-digit prime-like numbers that have 'm' repeated 'd's."""
  digits_except_d = range(d) + range(d+1, 10)
  for c in itertools.combinations_with_replacement(digits_except_d, n-m):
    digits = list(c) + [d]*m
    if sum(digits)%3 == 0:
      continue
    sd = set(digits)
    for h in sd:  # head
      if h == 0:
        continue
      d2 = list(digits)
      d2.remove(h)
      sd2 = set(d2)
      for r in sd2:  # rear
        if r%2 == 0:
          continue
        d3 = list(d2)
        d3.remove(r)
        for b in petools.Permutations(d3):  # body
          yield Dig2Num([h] + b + [r])


ans = 0
n = 10
primes = petools.Primes(100000)
for d in range(10):
  m = n
  while True:
    found = False
    for p in GenNums(n, m, d):
      if petools.IsPrime(p, primes):
        found = True
        ans += p
    if found:
      break
    m -= 1
print ans
