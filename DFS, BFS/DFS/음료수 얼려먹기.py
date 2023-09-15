import time

# N , M 입력
n, m = map(int, input().split())
start_time = time.time()

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        # 실수한점 y >= n 이라고 해버려서 가로축을 끝까지 검사 안해버려서 에러 뜸
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1 # 여기에서 방문처리를 하는 개념이기 때문에 굳이 visited 리스트를 따로 생성하지 않아도 된다.
        # 왜 이전 dfs 예제에서는 visited를 따로 생성했나?
        # -> 각 노드마다 특정 값을 가지고 있었기 때문에 그 값을 변경하지 못했다.
        # 그래서 따로 방문처리를 기록하는 visited 라는 리스트를 생성했던 것
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        # 주변 땅을 다 땅따먹기 하는 방식, 1,1을 검사했을때 주변 0으로 되어 있는 땅을 다 1로 만들고
        # True값 자체는 0,0에서만 반환할 수 있도록
        # 이미 따먹힌 땅은 검사해도 False 값을 뱉기 때문에 count 되지 않는다.
        print(x, y)
        return True
    return False


count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1


print(count)


