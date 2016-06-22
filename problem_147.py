import petools

@petools.Memorize
def CountRect(a, b, c, d):
  """Counts number of small rectangles inside a big (incomplete) rectangle.
  The input rectangle axb has 4 corners (two cxc/2, two dxd/2) cut."""
  vertex = [[1 for i in range(b+1)] for j in range(a+1)]  # a row, b col
  for i in range(c):  # cuts two c corners
    for j in range(i+1):
      vertex[j][i-j] = 0
      vertex[a-j][b-i+j] = 0
  for i in range(d):  # cuts two d corners
    for j in range(i+1):
      vertex[j][b-i+j] = 0
      vertex[a-j][i-j] = 0
  # Begins to count.
  count = 0
  for i in range(a+1):
    for j in range(b+1):
      if vertex[i][j] == 0:
        continue
      for p in range(i+1, a+1):
        if vertex[p][j] == 0:
          break
        for q in range (j+1, b+1):
          if vertex[i][q] == 0 or vertex[p][q] == 0:
            break;
          count += 1
  return count

def CountRect2(a, b):
  """Considers both cases: complete and incomplete."""
  a, b = min(a, b), max(a, b)
  return CountRect(a, b, 0, 0) + CountRect(a+b-2, a+b-2, a-2, b-2)

ans = 0
for a in range(47+1):
  print "a = %d" % a
  for b in range(43+1):
    ans += CountRect2(a, b)
print ans
