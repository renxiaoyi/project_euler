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


ans = 0
data = open('p105_sets.txt')
for line in data:
  line = line.strip()
  s = map(int, line.split(','))
  if IsSpecialSumSet(s):
    ans += sum(s)
print ans
