import math

data = open('p099_base_exp.txt')
cnt, max_num, ans = 0, 0, 0
for line in data:
  cnt += 1
  base_exp = map(int, line.strip().split(','))
  value = math.log(base_exp[0])*base_exp[1]
  if value > max_num:
    max_num = value
    ans = cnt
print ans
