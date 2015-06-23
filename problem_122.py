# Example:
#   exp = 15
#   mul = 5
#   path = [1, 2, 3, 6, 12, 15]
exp2mul = {1: 0}
paths = [[1]]
def OneStep():
  global paths
  paths_extended = []
  for p in paths:
    for n in p:
      exp = p[-1] + n
      mul = len(p)
      if exp not in exp2mul or mul <= exp2mul[exp]:
        exp2mul[exp] = mul
        paths_extended.append(p + [exp])
  paths = paths_extended


def Finished(max_exp, exp2mul):
  solved = sorted(exp2mul.keys())
  return len(solved) >= max_exp and solved[max_exp-1] == max_exp


max_exp = 200
while not Finished(max_exp, exp2mul):
  OneStep()
ans = sum(exp2mul[i] for i in range(1, max_exp+1))
print ans
