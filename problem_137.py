import math

# cnt = 0
# m, n = (1+math.sqrt(5))/2, 1+math.sqrt(2)
# p = 1
# known = set()
# while True:
#   for q in xrange(int(m*p), 1+int(n*p)):
#     u = p*q
#     d = q*q - p*q - p*p
#     if d < 0:
#       continue
#     if u % d != 0:
#       continue
#     nugget = u / d
#     if nugget in known:
#       continue
#     known.add(nugget)
#     cnt += 1
#     print p, q, nugget
#     if cnt == 15:
#       ans = u/d
#       break
#   if cnt == 15:
#     break
#   p += 1
# print ans

p, q = 1, 2
cnt = 1
while cnt <= 15:
  u = p*q
  d = q*q - p*q - p*p
  assert u % d == 0
  nugget = u / d
  print cnt, p, q, nugget
  p, q = p+q, p + 2*q
  cnt += 1
