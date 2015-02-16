import math

import petools

max_sum = 50000000
primes = petools.Primes(int(math.sqrt(max_sum)))
p2, p3, p4 = [], [], []
for p in primes:
  if p**2 <= max_sum: p2.append(p**2)
  if p**3 <= max_sum: p3.append(p**3)
  if p**4 <= max_sum: p4.append(p**4)
ans = set()
for i in p2:
  for j in p3:
    for k in p4:
      s = i + j + k
      if s <= max_sum:
        ans.add(s)
        #print i, j, k, s
print len(ans)
