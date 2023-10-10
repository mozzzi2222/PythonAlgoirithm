n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
result = 0
while start <= end:
    mid = (start+end) // 2
    total = 0
    for x in data:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
# 높이 H의 최댓값을 구하는 문제이므로 가능한 마지막에 기록된 mid를 담아야하므로 else함수로 해도 되는 것
        result = mid
        start = mid + 1
print(result)
