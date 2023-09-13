from collections import deque

def bfs(graph, start, visited):
    # 큐 생성
    queue = deque()
    # 시작 노드 큐에 추가
    queue.append(start)
    # 현재 노드 방문 처리
    visited[start] = True

    while queue:
        # 가장 먼저 들어온 원소 추출해서 v에 초기화
        v = queue.popleft()
        # 추출한 노드 출력
        print(v, end= " ")
        # 인접 노드 순회하며 방문처리 후 큐에 추가
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],  # 0
    [2, 3, 8],  # 1
    [1, 7],  # 2
    [1, 4, 5],  # 3
    [3, 5],  # 4
    [3, 4],  # 5
    [7],  # 6
    [2, 6, 8],  # 7
    [1, 7]  # 8
]

# 방문 처리를 위한 크기 9의 리스트 생성
visited = [False] * 9

bfs(graph, 1, visited)
