import petools


@petools.Memorize
def PermBlocks(m, n):
  assert n >= 0 and m >= 0
  if n < m:
    return 1
  else:
    return (PermBlocks(m, n-1)  # black first
            + sum(PermBlocks(m, n-i-1) for i in range(m, n))  # red+black first
            + 1)  # one red of length n


m, n = 50, 50
while PermBlocks(m, n) < 1000000:
  n += 1
print n
