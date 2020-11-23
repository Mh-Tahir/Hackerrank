"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    s = []
    for i in range(4):
        for k in range(4):
            u = arr[i][k] + arr[i][k + 1] + arr[i][k + 2] + arr[i + 1][k + 1] + arr[i + 2][k] + arr[i + 2][k + 1] + arr[i + 2][k + 2]
            s.append(u)
print(max(s))
