n = int(input())
array = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

count = [0] * (max(array) + 1)

for x in array:
    count [x] += 1

for x in data:
    if count[x] == 0:
        print('no', end = " ")
    else:
        print('yes', end = " ")
