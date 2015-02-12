import sets
import petools

min_k = 2
max_k = 12000
max_n = max_k * 2  # minimal product-sum number for k <= 2*k
k2n = {}
unique_n = sets.Set()
for n in range(2, max_n+1):
  for p in petools.Products(n):
    k = n - sum(p) + len(p)
    if k not in k2n:
      k2n[k] = n
for k, n in k2n.iteritems():
  if k < min_k or k > max_k:
    continue
  unique_n.add(n)
print sum(unique_n)
