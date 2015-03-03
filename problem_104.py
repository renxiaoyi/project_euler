import math

log_psi = math.log10((1+math.sqrt(5))/2)
log_sqrt5 = math.log10(math.sqrt(5))
mod = 10**9


def First9DigitsOfFib(n):
  exp = n*log_psi - log_sqrt5
  return int(pow(10, exp - int(exp) + 8))


def IsPandigital(s):
  l = map(int, s)
  l.sort()
  return l == range(1, 10)


a, b = 1, 1
i, j = 1, 2
while True:
  a, b = (a+b)%mod, (a+b+b)%mod
  i, j = j+1, j+2
  astr, bstr = str(a), str(b)
  if len(astr) >= 9 and IsPandigital(astr):
    if IsPandigital(str(First9DigitsOfFib(i))):
      ans = i
      break
  if len(bstr) >= 9 and IsPandigital(bstr):
    if IsPandigital(str(First9DigitsOfFib(j))):
      ans = j
      break
print ans
