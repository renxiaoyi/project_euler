import itertools


def IsSpecialSumSet(s):
  st = set()
  max_prev = max_this = 0
  for i in range(len(s)):
    for ss in itertools.combinations(s, i+1):
      sm = sum(ss)
      if sm <= max_prev:
        return False
      if sm in st:
        return False
      else:
        st.add(sm)
      max_this = max(max_this, sm)
    max_prev = max_this
  return True


def Try(cand):
  if len(cand) == cardinality and IsSpecialSumSet(cand):
    solutions.append(cand)
  if len(cand) < cardinality and IsSpecialSumSet(cand):
    if len(cand) == 0:
      min_c, max_c = lower_a1, upper_a1
    else:
      min_c = cand[-1]+1
      max_c = (upper_sum-sum(cand))/(cardinality-len(cand))
      if len(cand) >= 2:
        max_c = min(max_c, cand[0]+cand[1]-1)
    for c in range(min_c, max_c+1):
      Try(cand+[c])


cardinality = 7
upper_set = [20, 31, 38, 39, 40, 42, 45]
upper_sum = sum(upper_set)
lower_a1 = 11
upper_a1 = upper_sum/cardinality
solutions = []
Try([])

min_sum, ans = upper_sum, ''
for s in solutions:
  if sum(s) <= min_sum:
    min_sum, ans = sum(s), ''.join(map(str, s))
print ans
