import scipy.linalg
# Better to use scipy.interpolate.lagrange().
# http://mathoverflow.net/questions/169083/lagrange-interpolation-and-integer-polynomials


def EvalPoly(coeff, n):
  r = 0
  for i in range(len(coeff)-1):
    r = (r+coeff[i])*n
  return r + coeff[-1]


def Solve(seq):
  mat = []
  for i in range(len(seq)):
    mat.append([(i+1)**e for e in reversed(range(len(seq)))])
  return scipy.linalg.solve(mat, seq).round().tolist()


def FirstIncorrectTerm(coeff, seq):
  for i in range(len(seq)):
    m = EvalPoly(coeff, i+1)
    if abs(m-seq[i]) > 10**-6:
      return m
  return 0


ans = 0
seq = []
for i in range(11):
  seq.append(EvalPoly([1,-1,1,-1,1,-1,1,-1,1,-1,1], i+1))
for i in range(len(seq)):
  coeff = Solve(seq[:i+1])
  fit = FirstIncorrectTerm(coeff, seq)
  ans += fit
print ans
