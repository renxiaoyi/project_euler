import itertools

import petools


def NumOfNonTrivialPairs(n):
  """Example: (a,b)(c,d) or (a,c)(b,d) are trivial, but (a,d)(b,c) is not."""
  assert n == n/2*2
  num = 0
  for seta in itertools.combinations(range(n), n/2):
    setb = [i for i in range(n) if i not in seta]
    altb = [True]*(n/2)
    for i in range(n/2):
      if seta[i] < setb[i]:
        altb[i] = False
    if any(altb) and not all(altb):
      num += 1
  return num/2


def NumOfTests(n):
  num = 0
  for i in range(1, n/2+1):
    num += petools.Combination(n, i*2) * NumOfNonTrivialPairs(i*2)
  return num


print NumOfTests(12)
