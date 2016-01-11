import math

# According to Law of cosines, p^2 + p*r + r^2 = c^2.
# Let c = r+k, => r = (p^2-k^2)/(2*k-p) and p > k > p/2 (k is even).
# Suppose p <= q <= r.
max_sum = 120000
d = {}  # p => set(r)
for p in range(1, max_sum/2+1):
    if p%10000 == 0:
        print p
    d[p] = set()
    mink = int(p/2)+1
    maxk = int((math.sqrt(3)-1)*p)  # so that r >= p
    for k in range(mink, maxk+1):
        if (p**2-k**2)%(2*k-p) == 0:
            q = (p**2-k**2)/(2*k-p)
            d[p].add(q)

ans = set()
for p in d.keys():
    for q in d[p]:
        if q in d and len(d[q]) > 0:
            for r in d[p].intersection(d[q]):
                if p + q + r > max_sum:
                    continue
                ans.add(p+q+r)
print sum(ans)
