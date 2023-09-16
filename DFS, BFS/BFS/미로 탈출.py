import time
from collections import deque

# n, m 과 2차원 배열 입력
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

print(graph)
#시간 측정
start_time = time.time()

moves = ['up', 'left', 'down', 'right']
dx = [-1 , 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(len(moves)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print(nx, ",", ny, "에서의 노드값", graph[nx][ny])

                queue.append((nx, ny))
    return graph[n-1][m-1]


print(bfs(0,0))
