cube = lambda x: x ** 3
def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    a = [0, 1]
    for i in range(2, n):
        a.append(a[i - 1] + a[i - 2])
    return a

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
