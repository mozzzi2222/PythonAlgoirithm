import time

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[j] > array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i, end = ' ')


