import itertools

import petools


def Eval(expression):
  stack = []
  for i in expression:
    if i == '+':
      stack.append(stack.pop() + stack.pop())
    elif i == '-':
      stack.append(-stack.pop() + stack.pop())
    elif i == '*':
      stack.append(stack.pop() * stack.pop())
    elif i == '/':
      try:
        stack.append(1.0/stack.pop() * stack.pop())
      except ZeroDivisionError:
        return None
    else:
      stack.append(i)
  return stack[0]


def FindExpressibleNumbers(abcd):
  targets = set()
  for abcd_perm in itertools.permutations(abcd):
    a, b, c, d = abcd_perm
    for ops in itertools.product('+-*/', repeat=3):
      o, p, s = ops
      targets.add(Eval([a, b, o, c, p, d, s]))
      targets.add(Eval([a, b, o, c, d, p, s]))
  return targets


def FindMaxN(abcd):
  targets = FindExpressibleNumbers(abcd)
  for i in range(1, max(targets)+1):
    if i not in targets:
      return i-1
  return i-1


ans = ((1, 2, 3, 4), 28)
abcds = itertools.combinations(range(1, 10), 4)
for abcd in abcds:
  n = FindMaxN(abcd) 
  if n > ans[1]:
    ans = (abcd, n)
print ans
  
