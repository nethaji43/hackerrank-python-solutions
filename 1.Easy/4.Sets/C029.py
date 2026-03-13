K = int(input())
s = list(map(int,input().split()))
feq = {}
for i in s:
    if i in feq:
        feq[i] += 1
    else:
        feq[i] = 1
        
for i in feq:
    if feq[i] == 1:
        print(i)
        break
