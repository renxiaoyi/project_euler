def SumOfDigits(num):
  ret = 0
  while num > 0:
    ret += num%10
    num /= 10
  return ret


def IsPow(m, n):
  if n <= 1:
    return False
  while m % n == 0:
    m /= n
  return m == 1


def Find(nd):  # nd: num of digits
  assert nd >= 2
  ret = set()
  for sd in range(2, 9*nd):  # ds: sum of digits
    cand = sd
    while True:
      if cand <= 10**(nd-1):
        cand *= sd
      elif cand >= 10**nd:
        break
      else:
        if IsPow(cand, SumOfDigits(cand)):
          ret.add(cand)
        cand *= sd
  return sorted(ret)


nd = 2
ans = []
target = 30
while True:
  ans += Find(nd)
  if len(ans) >= target:
    print ans[target-1]
    break
  nd += 1
