array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두번째 데이터부터 시작해야 하므로 1부터 시작
    for j in range(i, 0, -1): # i부터 1까지 감소하며 반복하는 반복문
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)