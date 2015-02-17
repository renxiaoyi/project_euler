max_perimeter = 10**9
#max_perimeter = 1000


def BruteForce():
  k = 1  # triangle (2k+1, 2k+1, 2k+2) or (2k+1, 2k+1, 2k)
  r = 1
  r2 = r*r
  ans = 0
  while True:
    cnt += 1
    if 6*k + 2 > max_perimeter:
      break
    small = (3*k+2)*k
    big = (3*k+1)*(k+1)
    if small > r2:
      while r*r < small:
        r += 1
      r2 = r*r
    elif small == r2:
      ans += 6*k+4
      r += 1
      r2 = r*r
    elif small < r2 and r2 < big:
      r += 1
      r2 = r*r
    elif big == r2:
      ans += 6*k+2
      r += 1
      r2 = r*r
    else:  # r2 > big
      while r2 > (3*k+1)*(k+1):
        k += 1
  print ans


def Quick():
  sides = [5, 17]
  ans = 5*3+1 + 17*3-1
  i = 1
  while True:
    s = sides[i]*4 - sides[i-1] - 2*(-1)**i
    sides.append(s)
    p = s*3 - (-1)**i
    if p > max_perimeter:
      break
    ans += p
    i += 1
  print ans


Quick()
