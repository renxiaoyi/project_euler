import itertools

squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
ans = set()
cnt = 0  # count for cases where two squares are the same

def GetVariants(s):
  if s[0] == '6':
    return [s, '9'+s[1]]
  if s[1] == '6':
    return [s, s[0]+'9']
  if s[1] == '9':
    return [s, s[0]+'6']
  return [s]


def AddSolutions(cube1, cube2):
  global cnt  # necessary before assignments
  cwr = itertools.combinations_with_replacement
  cube1s = [cube1+list(x) for x in cwr('0123456789', 6-len(cube1))]
  cube2s = [cube2+list(x) for x in cwr('0123456789', 6-len(cube2))]
  for i in cube1s:
    if (len(i) > len(set(i))):
      continue
    i.sort()
    for j in cube2s:
      if (len(j) > len(set(j))):
        continue
      j.sort()
      sol = ''.join(i) + ',' + ''.join(j)
      if sol not in ans:
        ans.add(sol)
        if i == j:
          cnt += 1


def AddOneSquare(cube1, cube2, n):
  if len(cube1) > 6 or len(cube2) > 6:
    return
  if len(cube1) > len(set(cube1)) or len(cube2) > len(set(cube2)):
    return
  if n == len(squares):
    AddSolutions(cube1, cube2)
    return
  for s in GetVariants(squares[n]):
    AddOneSquare(cube1+[s[0]], cube2+[s[1]], n+1)
    AddOneSquare(cube1+[s[1]], cube2+[s[0]], n+1)
    if s[0] in cube1:
      AddOneSquare(cube1, cube2+[s[1]], n+1)
    if s[1] in cube1:
      AddOneSquare(cube1, cube2+[s[0]], n+1)
    if s[0] in cube2:
      AddOneSquare(cube1+[s[1]], cube2, n+1)
    if s[1] in cube2:
      AddOneSquare(cube1+[s[0]], cube2, n+1)
    if (s[0] in cube1 and s[1] in cube2) or (s[1] in cube1 and s[0] in cube2):
      AddOneSquare(cube1, cube2, n+1)


AddOneSquare([], [], 0)
print (len(ans)+cnt)/2
