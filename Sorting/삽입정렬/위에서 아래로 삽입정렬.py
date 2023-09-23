import time


n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

start_time = time.time()

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] > array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for i in array:
    print(i, end=' ')

end_time = time.time()
print(end_time - start_time)


