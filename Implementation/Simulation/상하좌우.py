# 시간 측정
import time

# 입력
n = int(input())
plan = list(input().split())

# 시간측정
start_time = time.time()

point_x = 1
point_y = 1

# 소스코드
for i in plan:
    if i == 'R':
        if point_y == n:
            continue
        point_y += 1
    elif i == 'L':
        if point_y == 1:
            continue
        point_y -= 1
    elif i == 'U':
        if point_x == 1:
            continue
        point_x -= 1
    elif i == 'D':
        if point_x == n:
            continue
        point_x += 1

print(f"{point_x} {point_y}")



end_time = time.time()
print(f"수행 시간 : {end_time - start_time}")