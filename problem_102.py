import scipy
import scipy.linalg


def Area(a, b):
  return scipy.linalg.norm(scipy.cross(a, b))/2


def ContainsOrigin(a, b, c):
  eps = 10**-6
  return abs(Area(a, b) + Area(b, c) + Area(c, a) - Area(a-c, b-c)) < eps


ans = 0
data = open('p102_triangles.txt')
for line in data:
  line = line.strip()
  if not line:
    continue
  coords = map(int, line.split(','))
  a = scipy.array(coords[0:2])
  b = scipy.array(coords[2:4])
  c = scipy.array(coords[4:])
  if ContainsOrigin(a, b, c):
    ans += 1
print ans
