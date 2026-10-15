from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

start = input("Enter starting node: ")

q = deque([start])
visited = {start}

while q:
    node = q.popleft()
    print(node, end=" ")

    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            q.append(n)
