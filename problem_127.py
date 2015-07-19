max_c = 120000-1
factors = [set() for _ in range(max_c+1)]
rad = [1]*(max_c+1)
for i in range(2, max_c+1):
    if rad[i] > 1:
        continue
    for j in range(i, max_c+1, i):
        rad[j] *= i
        factors[j].add(i)
ans = 0
cnt = 0
for a in range(1, max_c/2):  # slow, but works
    if a % 100 == 0: print a
    for b in range(a, 1+max_c-a):
        if (rad[a]*rad[b] < b and
            rad[a]*rad[b]*rad[a+b] < a+b and
            factors[a].isdisjoint(factors[b])):
            cnt += 1
            ans += a+b
print ans, cnt
