import math

import petools

max_num = 10**6


def BruteForce():
  primes = petools.Primes(max_num)
  spd = [-1]*(max_num+1)  # sum of proper divisors
  spd[0] = 0
  for i in primes:
    spd[i] = 1
  ans = (0, [])
  for i in range(1, max_num+1):
    if spd[i] >= 0:
      continue
    spd[i] = sum(petools.Divisors(i, primes)) - i
    track = [i]
    j = spd[i]
    while j <= max_num and spd[j] < 0 and j not in track:
      track.append(j)
      spd[j] = sum(petools.Divisors(j, primes)) - j
      j = spd[j]
    if j in track:  # e.g. track = [1, 2, 3, 4, 5], j = 3
      idx = track.index(j)
      chain = len(track) - idx
      if chain > ans[0]:
        ans = (chain, track[idx:])
  print ans


def Quick():
  primes = petools.Primes(max_num)
  spd = [-1]*(max_num+1)  # sum of proper divisors
  spd[0] = 0
  spd[1] = 0
  for i in primes:
    spd[i] = 1
  for n, f in petools.GenComposites(primes, max_num):
    spd[n] = sum(petools.DivisorsInter(*petools.Group(f))) - n

  for i in range(len(spd)):
    assert spd[i] > -1

  chains = [-1]*(max_num+1)
  ans = (0, [])
  for i in range(max_num+1):
    if chains[i] >= 0:
      continue
    track = [i]
    t = spd[i]
    while t <= max_num and chains[t] < 0 and t not in track:
      track.append(t)
      t = spd[t]
    if t > max_num or chains[t] >= 0:
      for r in track:
        chains[r] = 0
    else:  #t in track, e.g. track = [1, 2, 3, 4, 5], t = 3
      idx_t = track.index(t)
      chain_length = len(track) - idx_t
      for j in range(idx_t):
        chains[track[j]] = 0
      for j in range(idx_t, len(track)):
        chains[track[j]] = chain_length
      if chain_length > ans[0]:
        ans = (chain_length, track[idx_t:])
  print ans

Quick()
