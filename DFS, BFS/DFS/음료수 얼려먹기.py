import time

# N , M 입력
n, m = map(int, input().split())
start_time = time.time()

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False




graph = [list(map(int, input())) for _ in range(n)]

visited = [[False] * m] * n

print(graph)


