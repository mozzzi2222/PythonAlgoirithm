n = int(input())
array = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

array = sorted(array)
for x in data:
    start = 0
    end = max(array)
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == x:
            print("yes", end = " ")
            break
        elif array[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    if array[mid] == x:
        continue
    print('no', end = " ")

