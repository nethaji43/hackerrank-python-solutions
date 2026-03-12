n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for i in student_marks:
    if query_name == i:
        score = student_marks[query_name]
result = sum(score)/len(score)
print(f"{result:.2f}")
