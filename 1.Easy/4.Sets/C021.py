M = input()
lis = set(map(int, input().split()))
N = input()
lis1 = set(map(int,input().split()))
sym = lis.symmetric_difference(lis1)
sym = list(sym)
sym.sort()
for i in sym:
    print(i)