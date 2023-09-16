import time

# n, m 과 2차원 리스트 입력
n ,m = map(int, input().split())

# DFS로 구현해보니
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

start_time = time.time()

moves = ['up', 'left', 'down', 'right']
dx = [-1 , 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    for i in range(len(moves)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            print(nx,",", ny, "에서의 노드값",graph[nx][ny])
            dfs(nx, ny)
            # dfs로 구현시 이상한 결과값이 나온다.
    return graph[n-1][m-1]

print(dfs(0,0))