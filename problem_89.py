c2n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def Rom2Num(rom):
  nums = [c2n[c] for c in rom]
  i = 0
  while i < len(nums)-1:
    for j in range(i+1, len(nums)):
      if nums[j] != nums[i]:
        break
    if nums[j] > nums[i]:
      for k in range(i, j):
        nums[k] *= -1
    i = j
  return sum(nums)


nr = [
    (1000, 'M'), (900, 'CM'), (500, 'D'),  (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]


def Num2Rom(num):
  rom = ''
  for t in nr:
    n, r = t
    while num >= n:
      num -= n
      rom += r
  return rom


data = open('p089_roman.txt')
ans = 0
for l in data:
  l = l.strip()
  if not l:
    continue
  ans += len(l) - len(Num2Rom(Rom2Num(l)))
print ans
