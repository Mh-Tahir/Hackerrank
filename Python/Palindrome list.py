# Any palindrome and all positive elements in a list check
n = input()
k = input().split()
print(all([int(i) > 0 for i in k]) and any([j == j[::-1] for j in k]))

