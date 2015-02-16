import itertools

ans = 0
max_coord = 51
for p1 in itertools.product(range(max_coord), range(max_coord)):
  x1, y1 = p1
  if x1 == y1 == 0:
    continue
  for p2 in itertools.product(range(max_coord), range(max_coord)):
    x2, y2 = p2
    if (x2 == y2 == 0) or (x1 == x2 and y1 == y2):
      continue
    x3, y3 = x2-x1, y2-y1
    if x1*x2 + y1*y2 == 0 or x1*x3 + y1*y3 == 0 or x2*x3 + y2*y3 == 0:
      ans += 1
print ans/2
