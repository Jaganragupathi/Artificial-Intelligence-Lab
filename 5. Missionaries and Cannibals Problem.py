from collections import deque

start = (3, 3, 0)
goal = (0, 0, 1)

moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def safe(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

q = deque([(start, [])])
visited = {start}

while q:
    state, path = q.popleft()
    m, c, boat = state

    if state == goal:
        for s in path + [state]:
            print(s)
        break

    for dm, dc in moves:
        if boat == 0:
            ns = (m-dm, c-dc, 1)
        else:
            ns = (m+dm, c+dc, 0)

        if safe(ns[0], ns[1]) and ns not in visited:
            visited.add(ns)
            q.append((ns, path + [state]))
