def binary_search(array, target, start, end):
	if start>end: # 리스트 내에 찾는 원소가 없어 start가 end보다 커지는 상황
		return None
	mid = (start + end) // 2
	# 찾은 경우 중간점 인덱스 반
	if array[mid] == target:
		return mid
	# 중간점의 값보다 찾고자 하는 값이 더 큰 경우 끝점을 (중간점 -1) 로 변경하며 재귀함수
	elif array[mid] > target:
		return binary_search(array, target, start, mid - 1)
	# 중간점의 값보다 target이 더 작은 경우 시작점을 (중간점 +1)로 변경하여 재귀함수
	else:
		return binary_search(array, target, mid +1, end)

# 입력
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색 수행결과
result = binary_search(array, target, 0, n-1)
if result == None:
	print("해당 원소가 존재하지 않습니다.")
else:
	print(result + 1) # 몇번째에 있다고 출력 (인덱스 값이므로 +1)