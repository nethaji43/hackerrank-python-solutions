N = int(input())
result = []
for i in range(N):
    operation = list(input().split(" "))
    if operation[0] == 'insert':
        result.insert(int(operation[1]), int(operation[2]))
    elif operation[0] == 'print':
        print(result)
    elif operation[0] == 'remove':
        result.remove(int(operation[1]))
    elif operation[0] == 'append':
        result.append(int(operation[1]))
    elif operation[0] == 'sort':
        result.sort()
    elif operation[0] == 'pop':
        result.pop()
    elif operation[0] == 'reverse':
        result.reverse()
