import time

n ,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

start_time = time.time()

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(x, y):
    if graph[x][y] == 1:
        return False
    graph[x][y] = 1

    for i in range(4):
        nx = x - moves[i][0]
        ny = y - moves[i][1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            dfs(nx, ny)
    return True

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)

