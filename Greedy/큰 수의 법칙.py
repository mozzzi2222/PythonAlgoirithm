N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

largest = data[0]
second = data[1]
result = 0

while True:
    if M == 0:
        break
    for i in range(K):
        result += largest
        M -= 1
        if M == 0:
            break
    result += second
    M -= 1

print(result)




