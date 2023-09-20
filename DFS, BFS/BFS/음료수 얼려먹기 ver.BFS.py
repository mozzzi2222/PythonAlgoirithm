import time
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

start_time = time.time()

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    if graph[x][y] == 1:
        return False
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + moves[i][0]
            ny = y + moves[i][1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append((nx, ny))
    return True

count = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            count += 1
print(count)




