def wrap(string, max_width):
    result = []
    for i in range(0,len(list(string)),max_width):
        result.append(string[i:i+max_width])
    result = "\n".join(result)
    return result
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)