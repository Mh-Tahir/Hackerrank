#Mean, Median, and Mode (if more than one mode exists, mode is the numerically smallest one)
import statistics

num = int(input())
arr = [int(i) for i in input().split()]
print(statistics.mean(arr))
print(statistics.median(arr))
a = [arr.count(n) for n in arr]
m = max(a)
b = []
for n in arr:
    if arr.count(n) == m and n not in b:
        b.append(n)
print(min(b))
