# (2, 1) is the fundamental solution to the Pell's equation m^2 - 5*l^2 = -1.
# Trying to find all l that make positive interger value of a = (m+-2)/5.
m1, l1 = 2, 1
m, l = m1, l1
n = 5
cnt = 0
ans = 0
while True:
  m, l = m1*m + n*l1*l, m1*l + l1*m
  if m*m - 5*l*l == -1 and (m%5 == 2 or m%5 == 3):
    cnt += 1
    ans += l
    print cnt, l
  if cnt == 12:
    break
print ans
