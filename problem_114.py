import math

import petools


def PermBlocks(blocks):
  """Example: input [3, 3, 1] => output 1; [3, 1, 1, 1, 1] => 5."""
  blocks.append(1)  # "blocks" is sorted
  size2cnt = {}  # extended blocks
  for s in blocks:
    if s not in size2cnt:
      size2cnt[s] = 1
    else:
      size2cnt[s] += 1
  if 1 not in size2cnt:
    return 0
  nblack = size2cnt[1]
  nred = len(blocks) - nblack
  nblack_remained = nblack - nred  # extend each red with one black
  if nblack_remained < 0:
    return 0
  perm_cnt = petools.Product(range(nblack_remained+1, nred+nblack_remained+1))
  for s,c in size2cnt.iteritems():
    if s > 1 and c > 1:
      perm_cnt /= math.factorial(c)
  return perm_cnt
  

def Split(n, mlist, sol):
  """Generates lists using elements in 'mlist' that sum to 'n'."""
  if n == 0:
    yield sol
    return
  if len(mlist) == 0:
    return
  mlist2 = list(mlist[1:])
  if n >= mlist[0]:
    for s in Split(n-mlist[0], mlist, sol+[mlist[0]]):
      yield s
    for s in Split(n, mlist2, sol):
      yield s
  else:
    for s in Split(n, mlist2, sol):
      yield s


def FillRow(m, n):
  """m: min length of red blocks; n: row length"""
  mlist = range(n, m-1, -1) + [1]
  ans = 0
  for sol in Split(n, mlist, []):
    ans += PermBlocks(sol)
  return ans


print FillRow(3, 50)
