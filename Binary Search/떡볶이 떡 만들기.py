import time


start_time = time.time()

def binary_search(data, m, start, end):
    if start > end:
        return None
    total = 0
    mid = (start + end) // 2
    # 잘린 떡의 길이 계산
    for cake in data:
        if cake > mid:
            total += cake - mid
    # 잘린 떡이 얻고자 하는 양보다 적을 경우
    if total < m:
        return binary_search(data, m, start, mid - 1)
    # 잘린 떡이 얻고자 하는 양보다 클 경우
    else:
        return binary_search(data, m, mid+1, end)
    return mid
n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

result = binary_search(data, m, start, end)
print(result)

