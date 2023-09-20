import time

import time

n ,m = map(int, input().split())

visited = [[False] * m] * n
print(visited)

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

start_time = time.time()

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(x, y):
    if visited[x][y] == True or graph[x][y] == 1:
        return False
    visited[x][y] = True

    for i in range(4):
        nx = x - moves[i][0]
        ny = y - moves[i][1]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 0:
            dfs(nx, ny)
    return True

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            print(i, j)
            count += 1

print(count)

