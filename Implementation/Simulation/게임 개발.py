import time

start_time = time.time()

n, m = map(int, input().split())

a, b, d = map(int, input().split())

# 맵 입력하기
array = [list(map(int, input().split())) for _ in range(n)]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]

count = 1
turn_time = 0
while True:
    nx = a + moves[d][0]
    ny = b + moves[d][1]

    if array[nx][ny] == 1:
        turn_time += 1
        turn_left()
    else:
        array[a][b] = 1
        a = nx
        b = ny
        turn_time = 0
        count += 1
        continue

    if turn_time == 4:
        nx = a - moves[d][0]
        ny = b - moves[d][1]
        if array[nx][ny] == 1:
            break
        else:
            a = nx
            b = ny
            turn_time = 0

# for i in range(len(direction)):
#     # turn_left()
#     if direction[i] == d:
#         nx = a + moves[i][0]
#         ny = b + moves[i][1]
#         if array[nx][ny] == 1:
#             turn_time += 1
#         else:
#             a = nx
#             b = ny
#             count += 1
#             turn_time = 0
#
#         if turn_time == 4:
#             a = a - moves[i][0]
#             b = b - moves[i][1]

print(count)



