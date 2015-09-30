# (a, b, c) = (a, a+d, k*d), then a = d*(sqrt(2*k^2-1) - 1)/2.
# Solve the Pell's equation m^2 - 2*k^2 = -1.
m1, k1 = 1, 1
m, k = m1, k1
n = 2
maxp = 10**8
ans = 0
while True:
  m, k = m1*m + n*k1*k, m1*k + k1*m
  if m*m - 2*k*k == -1 and m > 1 and m%2 == 1:
    # p = d*(m+k), d = 1, 2, 3, ...
    inc = maxp / (m+k)
    ans += inc
    print '(%d, %d, %d), %d' % ((m-1)/2, (m+1)/2, k, inc)
    if inc == 0:
      break
print ans
