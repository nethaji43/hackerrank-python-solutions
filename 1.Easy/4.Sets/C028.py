N = int(input())
s = set(map(int,input().split()))
M = int(input())
for i in range(M):
    operation = list(input().split())
    if operation[0] == "intersection_update":
        h = set(map(int,input().split()))
        s.intersection_update(h)
    elif operation[0] == "update":
        h = set(map(int,input().split()))
        s.update(h)
    elif operation[0] == "symmetric_difference_update":
        h = set(map(int,input().split()))
        s.symmetric_difference_update(h)
    elif operation[0] == "difference_update":
        h = set(map(int,input().split()))
        s.difference_update(h)
print(sum(s))