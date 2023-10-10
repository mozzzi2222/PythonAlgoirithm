from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
def count_by_range(array, x):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)
    return right_index - left_index

count = count_by_range(data, m)

if count == 0:
    print(-1)
else:
    print(count)





