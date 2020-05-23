import math

# number of numbers in input
n = int(input())

# checks whether a number is prime
def check(i):
    if i <= 1:
        return 'Not prime'
    else:
        for k in range(2, int(math.sqrt(i)) + 1):
            if i % k == 0:
                return 'Not prime'
        return 'Prime'

for _ in range(n):
    print(check(int(input())))
