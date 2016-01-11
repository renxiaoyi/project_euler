import math
import fractions

# n = r + d*q, where q/d = d/r = c > 1.
# Let c = a/b and gcd(a, b) = 1, then b^2|r.
# 10^12 > n > d*q > r^2 => r < 10^6 => b < 10^3.
ans = set()
for b in range(1, 1001):
    for r in range(b*b, 10**6, b*b):
        a = b + 1
        while True:
            while fractions.gcd(a, b) != 1:
                a += 1
            d, q = r/b*a, r/(b*b)*a*a
            n = r + d*q
            if n > 10**12:
                break
            if int(math.sqrt(n))**2 == n:
                ans.add(n)
                print q, d, r, n
            a += 1
print sum(ans)
