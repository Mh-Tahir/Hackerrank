def swap_case(s):
    s = list(s)
    i = 0
    for i in range(len(s)):
        if s[i] == s[i].upper():
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()
    return ''.join(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
