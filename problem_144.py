import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Given Points f&h, returns Point t (from -> hit -> to).
def Calc(f, h):
    m = -4*h.x/h.y
    n = (-m*(f.x-h.x) + (f.y-h.y)) / math.sqrt((f.x-h.x)**2 + (f.y-h.y)**2)
    a, b, c = n**2-1, 2*m, n**2-m**2
    si = (f.y-h.y)/(f.x-h.x)  # slope of input
    so = -b/a - si  # slope of output
    p = h.y - so*h.x  # output line: y = so*x + p
    a, b, c = so**2+4, 2*so*p, p**2-100
    x = -b/a - h.x
    y = so*x + p
    return Point(x, y)

f, h = Point(0.0, 10.1), Point(1.4, -9.6)
ans = 1
while True:
    t = Calc(f, h)
    if 0.01 >= t.x >= -0.01 and t.y > 0:
        break
    f, h = h, t
    ans += 1
print ans
