n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))



# 기본 정렬 라이브러리 사용
sort_array = sorted(array, reverse= True)

for x in sort_array:
    print(x, end= " ")
