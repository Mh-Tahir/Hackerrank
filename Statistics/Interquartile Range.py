# Interquartile Range
import statistics

num = int(input())
a = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]
arr = []
for i, k in zip(a, w):
    for _ in range(k):
        arr.append(i)
arr = sorted(arr)
l = len(arr)
if l % 2 == 0:
    q1 = statistics.median(arr[:int(l / 2)])
    q3 = statistics.median(arr[int(l / 2):])
else:
    q1 = statistics.median(arr[:int((l - 1) / 2)])
    q3 = statistics.median(arr[int((l - 1) / 2 + 1):])
print(round(float(q3 - q1), 1))
