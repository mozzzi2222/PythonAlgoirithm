arr = [4, 3]
print(arr[2])

array = list(map(int, input().split()))

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    print(f"현재 피봇 : {array[pivot]}")
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            print(f"{array[left]}가 pivot보다 작습니다. left를 1 증가합니다.")
            left += 1
        while right > start and array[right] >= array[pivot]:
            print(f"{array[right]}가 pivot보다 작습니다. right를 1 감소합니다.")
            right -= 1
        if left > right:
            print(f"left가 rihgt보다 크네요. pivot({array[pivot]})과 right({array[right]})를 바꿉니다.")
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
