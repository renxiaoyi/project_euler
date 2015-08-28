max_n = 1000000
sol_n = [0]*max_n
for i in range(1, max_n):
  j = 1
  n = i*j
  while n < max_n:
    if (i+j) % 4 == 0:
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
  if sol_n[n] == 20:
    ans += 1
    print n
print ans
