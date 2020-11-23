# Output the integer number indicating the total number of occurrences of the substring in the original string.
def count_substring(string, sub_string):
    found = string.find(sub_string)
    if found == -1:
        return 0
    if string[found + 1:].find(sub_string) == -1:
        return 1
    else:
        return count_substring(string[found + 1:], sub_string) + 1
    return found

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
