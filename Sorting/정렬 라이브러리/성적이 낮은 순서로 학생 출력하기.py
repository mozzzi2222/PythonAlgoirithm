import time

n = int(input())
array = []

for _ in range(n):
    array.append(tuple(input().split()))

array = sorted(array, key = lambda x: x[1])

for i in array:
    print(i[0], end = ' ')
