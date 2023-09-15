from collections import deque
import time

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

start_time = time.time()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
moves = ['up', 'left', 'down', 'right']
def bfs(x ,y):
    queue = deque()
    queue.append((x,y))

    if graph[x][y] == 1:
        return False

    while queue:
        qx, qy = queue.popleft()
        graph[qx][qy] = 1
        for i in range(len(moves)):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                queue.append((nx, ny))
    return True

count = 0

for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            count += 1

print(count)




