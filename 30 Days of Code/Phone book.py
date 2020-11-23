n = int(input())
d = dict(input().split() for _ in range(n))
while True:
    try:
        i = input()
        print(i + '=' + d[i])
    except KeyError:
        print('Not found')
    except:
        break
