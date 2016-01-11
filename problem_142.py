import math

def IsPerfectSquare(n):
    return int(math.sqrt(n))**2 == n

# Looks for l, m, n, where l, m, l+m, n, m+n, l+m+n are all squares.
# y-z, x-y, y+z = l, m, n => x+y+z = m+n+(l+n)/2 (n > l && n+l is even)
lens = 1000
squares = [i*i for i in range(1, lens+1)]
for i in range(0, lens):
    m = squares[i]
    for j in range(0, lens):
        l = squares[j]
        if not IsPerfectSquare(l + m):
            continue
        for k in range(j, lens, 2):
            n = squares[k]
            if not IsPerfectSquare(m + n):
                continue
            if not IsPerfectSquare(l + m + n):
                continue
            print m+n+(l+n)/2

            
