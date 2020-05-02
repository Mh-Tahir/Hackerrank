# Performs append, pop, popleft and appendleft methods
from collections import deque
d = deque()
n = int(input())
for i in range(n):
    x = input().split()
    if x[0] == 'append':
        d.append(x[1])
    if x[0] == 'appendleft':
        d.appendleft(x[1])
    if x[0] == 'pop':
        d.pop()
    if x[0] == 'popleft':
        d.popleft()
print(' '.join(d))
