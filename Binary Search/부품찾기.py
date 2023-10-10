import time
# 수행시간 측정
start_time = time.time()

n = int(input())
array = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

array = sorted(array)
def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return False
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

start = 0
end = max(array)
for x in data:
    if binary_search(array, x, start, end) == True:
        print('yes', end = " ")
    else:
        print('no',  end = " ")
