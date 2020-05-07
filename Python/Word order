"""
You are given n words. 
Some words may repeat. 
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
"""
d = {}
n = int(input())
for i in range(n):
    x = input()
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
print(len(d))
for i in d:
    print(d[i], end=" ")
