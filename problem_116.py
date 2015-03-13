import petools


@petools.Memorize
def PermBlocks(m, n):
  if n < m:
    return 0
  else:
    return (PermBlocks(m, n-1)  # black first
            + PermBlocks(m, n-m)  # red first + black
            + 1)  # only one red


n = 50
print PermBlocks(2, n) + PermBlocks(3, n) + PermBlocks(4, n)

