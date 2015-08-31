max_n = 50*10**6
sol_n = [0]*max_n
for i in xrange(1, max_n):
  if i % 100000 == 0:
    print i
  j = 1
  n = i*j
  while n < max_n:
    if (i+j) % 4 == 0 and sol_n[n] <= 2:
      if i == j:
        sol_n[n] += 2
      elif i >= j:
        if 3*j > i:
          sol_n[n] += 2
        else:
          sol_n[n] += 1
      else:
        if 3*i > j:
          sol_n[n] += 2
        else:
          sol_n[n] += 1
    j += 1
    n = i*j

ans = 0
for n in range(1, max_n):
  if sol_n[n] == 2:
    ans += 1
print ans
