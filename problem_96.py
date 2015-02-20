import itertools

import petools


def Accept(sudoku, row, column, num):
  if num not in sudoku[row]:
    if num not in [sudoku[k][column] for k in range(9)]:
      for i,j in itertools.product(range(3), repeat=2):
        if sudoku[row/3*3+i][column/3*3+j] == num:
          return False
      return True
  return False


def Solve(sudoku):
  if 0 not in petools.Flatten(sudoku):
    return sudoku
  for i,j in itertools.product(range(9), repeat=2):
    if sudoku[i][j] == 0:
      copy = map(list, sudoku)
      for k in range(1, 10):
        if Accept(copy, i, j, k):
          copy[i][j] = k
          solution = Solve(copy)
          if solution:
            return solution
      return None


sudoku = [[] for i in range(9)]
data = open('p096_sudoku.txt')
ans = 0
for l in data:
  l = l.strip()
  if not l or l.startswith('Grid'):
    idx = 0
    continue
  sudoku[idx] = map(int, l)
  idx += 1
  if idx == 9:
    solution = Solve(sudoku)
    print solution
    ans += int(100*solution[0][0]+10*solution[0][1]+solution[0][2])
print ans
