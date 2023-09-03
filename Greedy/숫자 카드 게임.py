n, k = map(int, input().split())
data = []


for i in range(n):
    data.append(list(map(int, input().split())))

# 행렬중 가장 최소값들을 담기 위한 배열
least = []

# data 배열을 돌면서 least 배열에 각 행의 최솟값 담기
for i in data:
    least.append(min(i))

# least 배열 중 최댓값이 문제의 정답
result = max(least)

print(result)
    # 맨처음 작성했던 코드
    # data[i].sort()
    # if least < data[i][0]:
    #     least = data[i][0]



