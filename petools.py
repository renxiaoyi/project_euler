import math


# Returns all primes <= "max_num".
def Primes(max_num):
  is_prime = [True]*(max_num+1)
  is_prime[0] = False
  if max_num > 0: is_prime[1] = False
  for i in [x for x in range(int(math.sqrt(max_num))+1) if x > 1]:
    f = 2
    while i*f <= max_num:
      is_prime[i*f] = False
      f += 1
  return [x for x in range(max_num+1) if is_prime[x]]


def TestPrimes():
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  for i in range(50):
    actual = Primes(i)
    expected = [x for x in primes if x <= i]
    assert actual == expected


if __name__ == "__main__":
  TestPrimes()
  print "pass"
