import math
import petools

def Ring(r):  # returns a list of numbers in the r-th ring
  if r == 0:
    return 1
  return range(2+3*r*(r-1), 2+3*r*(r+1))

def Radius(n):  # returns r if n is in the r-th ring
  if n == 1:
    return 0
  r = int(math.sqrt((n-2)/3.0))
  while True:
    if 2 + 3*r*(r+1) > n:
      break
    r += 1
  return r

def AddEdge(r, ring, outer):
  min_k = 2 + 3*r*(r-1)
  for k in sorted(ring.keys()):
    idx = 0
    if k == min_k:
      ring[k].append(outer[0])
      ring[k].append(outer[1])
      ring[k].append(outer[-1])
      idx = 2
      continue
    ring[k].append(outer[idx])
    ring[k].append(outer[idx+1])
    idx += 2
    if (k-min_k) % r == 0:  # vertex
      ring[k].append(outer[idx+1])
      idx += 1

def InitRingd(ring):
  ringd = {c: [c-1, c+1] for c in ring[1:-1]}
  ringd[ring[0]] = [ring[1], ring[-1]]
  ringd[ring[-1]] = [ring[0], ring[-2]]
  return ringd

def AddEdge(ringd, c, ringd2, c2):
  ringd[c].append(c2)
  ringd2[c2].append(c)

# Too slow.
def Sol(target):
  primes = petools.Primes(1000000)
  def PD(n, ring):
    return len(filter(lambda x: abs(x-n) in primes, ring))
  cnt = 1  # PD(1) == 3
  print 1, 1
  ringd = {2:[1,3,7], 3:[1,2,4], 4:[1,3,5], 5:[1,4,6], 6:[1,5,7], 7:[1,2,6]}
  r = 0
  ans = 0
  while True:
    r += 1
    min_c = 2 + 3*r*(r-1)
    outer = Ring(r+1)
    ringd2 = InitRingd(outer)
    idx = 0  # index of numbers in the outer ring
    for c in sorted(ringd.keys()):  # loop through centers
      if c == min_c:
        AddEdge(ringd, c, ringd2, outer[0])
        AddEdge(ringd, c, ringd2, outer[1])
        AddEdge(ringd, c, ringd2, outer[-1])
        idx = 1
      else:
        AddEdge(ringd, c, ringd2, outer[idx])
        AddEdge(ringd, c, ringd2, outer[idx+1])
        idx += 1
        if (c-min_c) % r == 0:  # c is a vertex
          AddEdge(ringd, c, ringd2, outer[idx+1])
          idx += 1
      if PD(c, ringd[c]) == 3:
        assert c == min_c or c == max(ringd.keys())
        cnt += 1
        print cnt, c
        if cnt == target:
          ans = c
          break
    if ans > 0:
      break
    ringd = ringd2
  print ans

def Sol2(target):
  cnt = 2  # PD(1) == PD(2) == 3
  print 1, 1
  print 2, 2
  r = 1
  c1, c2 = 2+3*r*(r-1), 1+3*r*(r+1)
  c3, c4 = 2+3*(r+1)*r, 1+3*(r+1)*(r+2)
  while cnt < target:
    r += 1
    c5, c6 = 2+3*(r+1)*r, 1+3*(r+1)*(r+2)
    # ring3 = [c4, c5+1, c6]  # c1, c3-1, c5 omitted
    # ring4 = [c1, c3, c6-1]  # c2, c4-1, c6 omitted
    if petools.IsPrime(c4 - c3):
      if petools.IsPrime(1+c5-c3) and petools.IsPrime(c6-c3):
        cnt += 1
        print cnt, c3
        if cnt == target:
          ans = c3
      if petools.IsPrime(c4-c1) and petools.IsPrime(c6-c4-1):
        cnt += 1
        print cnt, c4
        if cnt == target:
          ans = c4
    c1, c2 = c3, c4
    c3, c4 = c5, c6
  print ans

Sol2(2000)
