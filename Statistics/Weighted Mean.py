#Weighted Mean (rounded to 1 decimal place)
n = int(input())
arr = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
s = sum([x * y for x, y in zip(arr, w)]) / sum(w)
print('{:.1f}'.format(s))
