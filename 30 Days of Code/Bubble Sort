n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps = 0

for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1

print('Array is sorted in {} swaps.'.format(swaps))
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')
