import petools

# DETERMINISTIC: SLOW (20min)
#
# # n^2 = 0 (mod 2).
# # n^2 = 1 (mod 3), because if n^2 = 2 (mod 3) then 3 | (n^2+7).
# # n^2 = 0 (mod 5).
# # n^2 = 2 or 3 (mod 7).
# #
# # Extend the idea above:
# # If prime p cannot divide any of n^2+[1, 3, 7, 9, 13, 27] and n%p = i,
# # then p cannot divide any of i^2+[1,3,7,9,13,27] (because n^2 = i^2 (mod p)).
# # (note p < n^2+x to avoid the exception p == n^2+x)
# # Therefore we can derive all possible remainders i.
# def ValidRemainders(p):
#   rem = []
#   for i in range(p):
#     if all((i*i+x)%p != 0 for x in [1, 3, 7, 9, 13, 27]):
#       rem.append(i)
#   return rem

# p2r = {}
# for p in petools.Primes(5000):
#   p2r[p] = ValidRemainders(p)
# limit = 150*10**6
# primes = petools.Primes(limit)
# ans = 0
# for n in range(10, limit, 10):  # n = 2 is excluded
#   if any(p <= n*n and n%p not in p2r[p] for p in p2r):
#     continue
#   s = n*n
#   if (all(petools.IsPrime(s+x, primes) for x in [1,3,7,9,13,27]) and
#       all(not petools.IsPrime(s+x, primes) for x in [11,17,19,21,23])):
#     print n
#     ans += n
# print "ans = %d" % ans


# PROBABILISTIC: FAST (2min)
limit = 150*10**6
p2r = {3:[1], 7:[2,3]}
ans = 0
for n in range(10, limit, 10):  # n = 2 is excluded
  s = n*n
  if any(p <= s and s%p not in p2r[p] for p in p2r):
    continue
  if (all(petools.RabinMiller(s+x, 10) for x in [1,3,7,9,13,27]) and
      all(not petools.RabinMiller(s+x, 10) for x in [11,17,19,21,23])):
    print n
    ans += n
print "ans = %d" % ans
