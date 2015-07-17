import petools

import heapq
import math

# ===
# Solution 1: too slow.

def Distance(p, q):
  assert(len(p) == len(q))
  return sum([(p[i]-q[i])**2 for i in range(len(p))])

def NextCandidate(quad):
  a, b, c, l = quad
  assert(a >= b >= c)
  yield (a, b, c, l+1)
  yield (a+1, b, c, l)
  if a >= b+1:
    yield (a, b+1, c, l)
  if b >= c+1:
    yield (a, b, c+1, l)

@petools.Memorize
def Shell(a, b, c, l):
  # The cuboid is composed by cubes (1,1,1), (1,1,2), ..., (a,b,c).
  shell = set()
  if l == 1:
    for x in range(1, a+1):
      for y in range(1, b+1):
        shell.add((x, y, 0))
        shell.add((x, y, c+1))
    for x in range(1, a+1):
      for z in range(1, c+1):
        shell.add((x, 0, z))
        shell.add((x, y+1, z))
    for y in range(1, b+1):
      for z in range(1, c+1):
        shell.add((0, y, z))
        shell.add((a+1, y, z))
  else:
    center = ((1+a)/2.0, (1+b)/2.0, (1+c)/2.0)
    inner_shell = Shell(a, b, c, l-1)
    is_outside = lambda p: Distance(p, center) > d and p not in inner_shell
    for cube in inner_shell:
      x, y, z = cube
      d = Distance(cube, center)
      if is_outside((x+1, y, z)):
        shell.add((x+1, y, z))
      if is_outside((x-1, y, z)):
        shell.add((x-1, y, z))
      if is_outside((x, y+1, z)):
        shell.add((x, y+1, z))
      if is_outside((x, y-1, z)):
        shell.add((x, y-1, z))
      if is_outside((x, y, z+1)):
        shell.add((x, y, z+1))
      if is_outside((x, y, z-1)):
        shell.add((x, y, z-1))
  return shell

def ShellVol(a, b, c, l):  # equivalent to len(Shell(a, b, c, l))
  return 2*(a*b+b*c+c*a) + 4*(a+b+c+l-2)*(l-1)

def C(wanted_n):
  heap = [(ShellVol(1,1,1,1), (1,1,1,1))]
  c = 0
  while True:
    n, quad = heapq.heappop(heap)
    if n > wanted_n:
      break
    if n == wanted_n:
      c += 1
    for q in NextCandidate(quad):
      nq = (ShellVol(*q), q)
      if nq not in heap:
        heapq.heappush(heap, nq)
  return c

def Sol(wanted_c):
  heap = [(ShellVol(1,1,1,1), (1,1,1,1))]
  current_c = 0
  current_n = 0
  ans = 0
  while True:
    n, quad = heapq.heappop(heap)
    if n > current_n:
      if current_c == wanted_c:
        ans = current_n
        break
      current_n = n
      current_c = 1
    elif n == current_n:
      current_c += 1
    for q in NextCandidate(quad):
      nq = (ShellVol(*q), q)
      if nq not in heap:
        heapq.heappush(heap, nq)
  return ans


# ===
# Solution 2: too slow.

def Solabc(x, y):
  # Returns number of positive integer solutions (a, b, c) for
  #   x = a*b + b*c + c*a;
  #   y = a + b + c;
  #   a >= b >= c.
  n = 0
  if y == None:
    r = int(math.sqrt(x/3))
    for a in range(r, 1+x/2):
      for c in range(1, 1+r):
        if x <= a*c or (x-a*c)%(a+c) != 0:
          continue
        b = (x-a*c)/(a+c)
        if a >= b >= c:
          n += 1
    return n
  if y > x or y*y < 2*x + 3:
    return 0
  r, s, t = y/3, int(math.sqrt(x/3)), int(math.sqrt((y*y-2*x)/3))
  for a in range(max(1,r,s,t), 1+min(y-2,(x-1)/2)):
    for c in range(1, 1+min(r,s,t)):
      b = y-a-c
      if a >= b >= c and x == a*b + b*c + c*a:
        n += 1
  return n

def Solxy(n, l):
  # Yields positive integer solutions (x, y) for
  #   2*x + 4*(l-1)*y + 4*(l-2)*(l-1) - n = 0,
  #   3 <= y <= x.
  a, b, c = 2, 4*(l-1), n - 4*(l-2)*(l-1)
  if b == 0:
    if n % 2 == 0:
      yield c/2, None
    return
  for y in range(3, 1+int(c/(a+b))):
    x = (c-b*y)/a
    if x < y:
      return
    if (c-b*y)%a == 0:
      yield x, y

def Sol2(wanted_c):
  n = 6
  while True:
    c = 0
    for l in range(1, 1+int(math.sqrt((n-2)/4))):
      for xy in Solxy(n, l):
        c += Solabc(*xy)
    if c == wanted_c:
      ans = n
      break
    n += 2
  print ans


# ===
# Solution 3: works.

max_n = 20000
n2c = {}
for n in range(1, 1+max_n):
  n2c[n] = 0

def Sol3(wanted_c):
  c = 1
  while ShellVol(c, c, c, 1) <= max_n:
    b = c
    while ShellVol(b, b, c, 1) <= max_n:
      a = b
      while ShellVol(a, b, c, 1) <= max_n:
        l = 1
        while ShellVol(a, b, c, l) <= max_n:
          n2c[ShellVol(a, b, c, l)] += 1
          l += 1
        a += 1
      b += 1
    c += 1
  for n in range(1, 1+max_n):
    if n2c[n] == wanted_c:
      return n
  return None

ans = Sol3(1000)
print ans
