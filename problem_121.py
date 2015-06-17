import petools


def P(k):  # probability(blue in the k-th turn)
  assert k > 0
  return 1.0/(k+1)


@petools.Memorize
def P2(m, n):  # probability(n blue in m turns)
  if not (m >= n >= 0):
    return 0
  if m == 0 and n == 0:
    return 1
  return P(m)*P2(m-1, n-1) + (1-P(m))*P2(m-1, n)


@petools.Memorize
def Pwin(m):  # probability(blue > red in m turns)
  assert m > 0
  return sum([P2(m, n) for n in range(m/2+1, m+1)])


ans = 1.0 / Pwin(15)
print int(ans)
