n, k = map(int, input().split())
data = []


for i in range(n):
    data.append(list(map(int, input().split())))

least = 0 # 행렬중 가장 최소값 담기 위한 변수

for i in range(n):
    if least < min(data[i]):
        least = min(data[i])

    # 맨처음 작성했던 코드
    # data[i].sort()
    # if least < data[i][0]:
    #     least = data[i][0]

print(least)

