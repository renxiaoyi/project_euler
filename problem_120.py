def Rmax(a):
  if a % 2 == 1:
    return a*(a-1)
  else:
    return a*(a-2)


ans = sum([Rmax(a) for a in range(3, 1001)])
print ans
