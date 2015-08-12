import petools

# maxp = 1000
# maxm = maxp
# cubes = [i**3 for i in range(maxm)]
# squares = [i*i for i in range(maxm)]

# def FindPartner(p):
#   r2n = {}
#   for i in range(1, maxm):
#     r = cubes[i] % p
#     if r in r2n:
#       r2n[r].append(i)
#     else:
#       r2n[r] = [i]
#   for k,v in r2n.iteritems():
#     if len(v) >= 2:
#       for n in v:
#         try:
#           m = cubes.index(cubes[n] + p*squares[n])
#           return n, m
#         except ValueError:
#           continue
#   return None, None

# primes = petools.Primes(maxp)
# for p in primes:
#   n, m = FindPartner(p)
#   if n:
#     print '%d^3 + %d*%d^2 = %d^3' % (n, p, n, m)

ans = 0
maxp = 10**5
for i in range(maxp):
  p = 3*i*i + 3*i + 1
  if p >= maxp:
    break
  if petools.IsPrime(p):
    ans += 1
print ans
