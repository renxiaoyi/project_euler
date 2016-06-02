# There are 4 possibilities for a + b (0 <= a, b <= 9):
#   0+: even with carry-over;
#   0-: even without carry-over;
#   1+: odd with carry-over;
#   1-: odd without carry-over.
# So consider abc...xyz + zyx...cba, from lowest=>highest=>lowest=>highest=>...
#   if a+z is 1+ => b+y=0- => c+x=1+ => ... and len(abc...xyz) is odd;
#     actually len(a...z) can only be 4*n-1, e.g. 3, 7, 11, ...
#   if a+z is 1- => b+y=1- => c+x=1- => ... and len(abc...xyz) is even.

def TypeOf(a, b):
    n = a + b
    if n%2 == 0:
        if n >= 10:
            return '0+'
        else:
            return '0-'
    else:
        if n >= 10:
            return '1+'
        else:
            return '1-'

# Number of ordered pairs (a, b) for each type:
zp = zm = op = om = 0  # 0+/0-/1+/1-
op0 = om0 = 0  # 1+/1- pairs that has at least one 0
for a in range(10):
    for b in range(a, 10):
        if TypeOf(a, b) == '0+':
            if a == b:
                zp += 1
            else:
                zp += 2
        elif TypeOf(a, b) == '0-':
            if a == b:
                zm += 1
            else:
                zm += 2
        elif TypeOf(a, b) == '1+':
            op += 2
            if a == 0:
                op0 += 2
        else:
            om += 2
            if a == 0:
                om0 += 2
assert zp+zm+op+om == 100

def CalcForLen(l):
    if l % 2 == 0:
        return (om-om0)*(om**(l/2-1))
    else:
        if (l+1) % 4 == 0:
            e = (l-3)/4
            return (op-op0)*5*(zm**e)*(op**e)
        else:
            return 0

def Check(l):
    cnt = 0
    for i in range(10**(l-1), 10**l):
        n = str(i)
        r = ''.join(n[k] for k in range(l-1, -1, -1))
        if r[0] == '0':
            continue
        s = str(i + int(r))
        if all(map(lambda x: int(x)%2==1, s)):
            cnt += 1
    return cnt

ans = 0
for l in range(1, 9):
    ans += CalcForLen(l)
print ans
