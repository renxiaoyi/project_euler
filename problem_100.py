import math

max_num = 10**12


def BruteForce():
  array = [i*(i+1) for i in range(max_num)]
  for i in range(max_num):
    if array[i]*2 in array:
      idx = array.index(array[i]*2)
      print i+1, idx+1


def Quick():
  ans = 0
  array = [1, 3]
  while True:
    value = 6*array[-1]-array[-2]-2
    array.append(value)
    if 1+math.sqrt(1+8*value*(value-1)) > 2*max_num:
      ans = value
      break
  print ans


Quick()
