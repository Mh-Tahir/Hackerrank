n = int(input())
s = set()
a = 0
for i in range(n):
    k = input()
    if k in s:
        a -= 1
    s.add(k)
print(n + a)
