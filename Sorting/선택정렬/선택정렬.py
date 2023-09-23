array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # min_index는 가장 작은 원소의 인덱스를 담는 변수
    for j in range(i+1, len(array)): # i 다음원소부터 검사 시작
        if array[min_index] > array[j]:
            min_index = j # j가 위에서 설정한 min_index보다 작으면 min_index를 j로 변경
    array[i], array[min_index] = array[min_index], array[i] # Swap : i와 찾은 min_index를 변경

print(array)