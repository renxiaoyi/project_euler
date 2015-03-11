def IsSorted(li):
  for i in range(len(li)-1):
    if li[i] > li[i+1]:
      return False
  return True


def IsBouncy(num):
  assert num > 0
  digits = []
  while num > 0:
    digits = [num%10] + digits
    num /= 10
  return not (IsSorted(digits) or IsSorted(digits[::-1]))


per = 99
cnt = 0
num = 1
while True:
  if IsBouncy(num):
    cnt += 1
  if num * per == cnt * 100:
    break
  num += 1
print num 
