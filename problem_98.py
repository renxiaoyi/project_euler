import itertools
import math


def MatchTups(tup1, tup2):
  def Match(w1, w2):
    if len(w1) != len(w2):
      return None
    dic = {}
    used = set()
    for i in range(len(w1)):
      if w1[i] not in dic:
        if w2[i] in used:
          return None
        dic[w1[i]] = w2[i]
        used.add(w2[i])
      else:
        if dic[w1[i]] != w2[i]:
          return None
    return dic
  # END def Match(w1, w2):
  dic1 = Match(tup1[0], tup2[0])
  if dic1:
    return Match(tup1[1], tup2[1]) == dic1
  dic2 = Match(tup1[0], tup2[1])
  if dic2:
    return Match(tup1[1], tup2[0]) == dic2
  return False


data = open('p098_words.txt').read()
words = [s[1:-1] for s in data.split(',')]
anagram_groups = [(i, {}) for i in range(100)]
for w in words:
  wlen, group = anagram_groups[len(w)]
  key = ''.join(sorted(w))
  if key not in group:
    group[key] = [w]
  else:
    group[key].append(w)

ans = 0
for wlen, group in reversed(anagram_groups):
  if len(group) == 0:
    continue
  anagrams = [x for _, x in group.iteritems() if len(x) >= 2]
  if len(anagrams) == 0:
    continue
  
  squares = {}
  for s in [str(i*i) for i in range(int(math.sqrt(10**(wlen-1)-1)+1),
                                    int(math.sqrt(10**wlen-1)+1))]:
    key = ''.join(sorted(s))
    if key in squares:
      squares[key].append(s)
    else:
      squares[key] = [s]
  squares = [x for _, x in squares.iteritems() if len(x) >= 2]
  if len(squares) == 0:
    continue

  for anag in anagrams:
    for tup1 in itertools.combinations(anag, 2):
      for squa in squares:
        for tup2 in itertools.combinations(squa, 2):
          if MatchTups(tup1, tup2):
            print tup1, tup2
            ans = max(ans, int(tup2[0]), int(tup2[1]))
  if ans > 0:
    break
print ans
