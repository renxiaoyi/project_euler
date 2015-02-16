ans = {}
cnt = 0


def Next(n):
  digits = map(int, str(n))
  squares = [x*x for x in digits]
  return sum(squares)


for i in range(1, 10000000):
  n = i
  chain = [n]
  while True:
    if n == 1 or n == 89:
      for j in chain:
        ans[j] = n
      break
    if n in ans:
      for j in chain:
        ans[j] = ans[n]
      break
    n = Next(n)
    chain.append(n)
  if ans[i] == 89:
    cnt += 1
print cnt
