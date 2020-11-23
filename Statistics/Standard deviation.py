# Standard deviation
n = int(input())
x = [int(x) for x in input().split()]
mean = sum(x) / n
y = [(x - mean) ** 2 for x in x]
sd = (sum(y) / n) ** 0.5
print(round(sd, 1))
