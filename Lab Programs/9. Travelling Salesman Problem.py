from itertools import permutations

n = int(input("Enter number of cities: "))

dist = []
for i in range(n):
    dist.append(list(map(int, input().split())))

cities = range(1, n)
min_cost = float("inf")
best_path = None

for p in permutations(cities):
    path = (0,) + p + (0,)
    cost = 0

    for i in range(len(path)-1):
        cost += dist[path[i]][path[i+1]]

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Best path:", best_path)
print("Minimum cost:", min_cost)
