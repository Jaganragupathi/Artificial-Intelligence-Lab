import heapq

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"D": 2, "E": 5},
    "C": {"E": 1},
    "D": {"G": 3},
    "E": {"G": 2},
    "G": {}
}

h = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 3,
    "E": 2,
    "G": 0
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

q = [(h[start], 0, start, [start])]
visited = set()

while q:
    f, cost, node, path = heapq.heappop(q)

    if node == goal:
        print("Path:", path)
        print("Cost:", cost)
        break

    if node in visited:
        continue

    visited.add(node)

    for n, c in graph[node].items():
        if n not in visited:
            new_cost = cost + c
            heapq.heappush(q, (new_cost + h[n], new_cost, n, path + [n]))
