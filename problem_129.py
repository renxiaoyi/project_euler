def Undividable(n, m):
  # Returns True if n divides none of {1, 11, 111, ... R(m)}.
  r = 1  # remainder 10^(i-1) % n
  rem = 1 # remainder R(i) % n
  for i in xrange(2, m+1):
    r = 10*r % n
    rem = (rem+r) % n
    if rem == 0:
      return False
  return True

def LeastN(m):
  n = m
  while True:
    n += 1
    if n % 2 == 0 or n % 5 == 0:
      continue
    if Undividable(n, m):
      return n

print LeastN(10**6)
