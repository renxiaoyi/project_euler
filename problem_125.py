import petools

maxn = 10**8
squares = []
l = 0
for i in range(1, maxn):
  s = i*i
  if s >= maxn:
    break
  squares.append(s)
  if sum(squares) < maxn:
    l = len(squares)
ans = set()
for i in range(len(squares)):
  for j in range(i+2, i+l):
    if j >= len(squares):
      break
    c = sum(squares[i:j])
    if c >= maxn:
      break
    if petools.IsPalindrome(str(c)):
      ans.add(c)
print sum(ans)
