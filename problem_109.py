singles = range(1, 21)
scores = ([[s] for s in singles] + [[25]] +
          [[s, s] for s in singles] + [[25, 25]] +
          [[s, s, s] for s in singles])
scores.sort(key=lambda s: -sum(s))


def Tuple2String(t):
  if len(t) == 1:
    return 'S' + str(t[0])
  if len(t) == 2:
    return 'D' + str(t[0])
  if len(t) == 3:
    return 'T' + str(t[0])


def NumberOfWaysToCheckout(s, slist, rec):
  if s == 0:
    return len(set([r for r in rec if len(rec) <= 3 and r[0] == 'D']))
  if len(slist) == 0 or len(rec) >= 3:
    return 0
  slist2 = list(slist[1:])
  if s >= sum(slist[0]):
    return (NumberOfWaysToCheckout(s-sum(slist[0]),
                                   slist,
                                   rec+[Tuple2String(slist[0])]) +
            NumberOfWaysToCheckout(s, slist2, rec))
  else:
    return NumberOfWaysToCheckout(s, slist2, rec);


ans = 0
for s in range(100):
  ans += NumberOfWaysToCheckout(s, scores, [])
print ans
