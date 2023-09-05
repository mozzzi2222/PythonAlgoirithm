n = int(input())
plans = input().split()

move_types = ['R', 'L', 'U', 'D']
mx = [0, 0, -1, 1]
my = [1, -1, 0, 0]

x, y = 1, 1

for plan in plans:
    for i in range(len(move_types)):
        if move_types[i] == plan:
            nx = x + mx[i]
            ny = y + my[i]
    # nx, ny가 범위 초과시 continue
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x = nx
    y = ny

print(x, y)
