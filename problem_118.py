import itertools

import petools


def Combine(t):
  ret = 0
  for i in t:
    ret *= 10
    ret += i
  return ret


def NumOfPrimesCat(s):
  if len(s) == 0:
    return 0
  if len(s) == 1:
    return int(s[0] in [2, 3, 5, 7])
  if sum(s) % 3 == 0:
    return 0
  if all([x % 2 == 0 for x in s]):
    return 0
  ret = 0
  for t in itertools.permutations(s):
    if petools.IsPrime(Combine(t)):
      ret += 1
  return ret


def Contains(full, seg):
  return all([x in full for x in seg])


def Diff(full, seg):
  d = [x for x in full if x not in seg]
  return ''.join(d)


def Part(full, segs):
  """full: sorted digit string; segs: list of sorted digit strings."""
  if full in segs:
    yield [full]
  for i in range(len(segs)):
    seg = segs[i]
    if Contains(full, seg):
      for p in Part(Diff(full, seg), segs[i+1:]):
        yield [seg] + p


d = {}
digits = range(1, 10)
for l in range(1, len(digits)+1):
  for t in itertools.combinations(digits, l):
    key = str(Combine(sorted(t)))
    val = NumOfPrimesCat(t)
    if val > 0:
      d[key] = val
ans = 0
for p in Part(str(Combine(digits)), d.keys()):
  ans += petools.Product([d[i] for i in p])
print ans
