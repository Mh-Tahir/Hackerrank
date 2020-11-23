# Using only arithmetic operations, a single for loop and print statement
'''
1
22
333
4444
55555
......
'''
for i in range(1, int(input())):
    print((10 ** i // 9) * i)
