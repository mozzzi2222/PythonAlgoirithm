n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0


for k in data:
    for j in range(k, m+1):
        if d[j - k] != 10001: # 사실 없어도 되는 코드
            d[j] = min(d[j], d[j - k] + 1)

if d[m]== 10001:
    print(-1)
else:
    print(d[m])



