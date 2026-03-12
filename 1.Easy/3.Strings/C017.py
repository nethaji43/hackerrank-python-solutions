def count_substring(string, sub_string):
    score = 0
    length = len(list(sub_string))
    count = len(list(string))
    for i in range(count):
        if sub_string[0]== string[i]:
            result = string[i:i+length]
            if result == sub_string:
                score += 1
    return score

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)