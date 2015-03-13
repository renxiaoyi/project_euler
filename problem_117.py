import petools


@petools.Memorize
def PermBlocks(n):
  if n < 0:
    return 0
  elif n < 2:
    return 1
  else:
    return (PermBlocks(n-1)  # black first
            + sum(PermBlocks(n-i) for i in range(2, 5)))  # colored first


print PermBlocks(50)
