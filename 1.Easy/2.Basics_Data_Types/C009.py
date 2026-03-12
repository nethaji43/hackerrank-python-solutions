records = []
scores = []
for i in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
    scores.append(score)
result = []
for i in scores:
    if i not in result:
        result.append(i)
result.sort()
second_lowest = result[1]
results=[]
for i in range(len(records)):
    if second_lowest == records[i][1]:
        results.append(records[i][0])
results.sort()
for i in results:
    print(i)