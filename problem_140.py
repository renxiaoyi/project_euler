# import math

# cnt = 0
# m = (math.sqrt(5)-1)/4
# n = m*2
# q = 1
# known = set()
# while True:
#   for p in xrange(int(m*q), 1+int(n*q)):
#     u = p*(3*p+q)
#     d = q*q - p*q - p*p
#     if u <= 0 or d <= 0:
#       continue
#     if u % d != 0:
#       continue
#     nugget = u / d
#     if nugget in known:
#       continue
#     known.add(nugget)
#     cnt += 1
#     print p, q, nugget
#     if cnt == 30:
#       ans = u/d
#       break
#   if cnt == 30:
#     break
#   q += 1
# print ans

A = lambda p, q: p*(3*p+q)/(q*q-p*q-p*p)
ans = 0
p, q, cnt = 1, 2, 1
while cnt <= 15:
  ans += A(p, q)
  p, q, cnt = p+q, p+q+q, cnt+1
p, q, cnt = 2, 5, 1
while cnt <= 15:
  ans += A(p, q)
  p, q, cnt = p+q, p+q+q, cnt+1
print ans
