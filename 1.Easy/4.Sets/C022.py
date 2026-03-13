N = int(input())
countries = set()
for i in range(N):
    countries.add(input())
countries = sorted(countries)
print(len(list(countries)))
