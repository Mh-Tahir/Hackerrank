# Calculate quartiles
import statistics

num = int(input())
arr = [int(i) for i in input().split()]
arr = sorted(arr)
l = len(arr)
q2 = statistics.median(arr)
if l % 2 == 0:
    q1 = statistics.median(arr[:int(l / 2)])
    q3 = statistics.median(arr[int(l / 2):])
else:
    q1 = statistics.median(arr[:int((l - 1) / 2)])
    q3 = statistics.median(arr[int((l - 1) / 2 + 1):])
print(round(q1))
print(round(q2))
print(round(q3))
