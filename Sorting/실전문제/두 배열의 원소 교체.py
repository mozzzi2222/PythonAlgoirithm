n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


min_index = 0
max_index = 0
while k > 0: # 이러면 k 횟수가 남아있어도 a가 b의 원소보다 모두 커서 바꿀 필요가 없는데 굳이 바꿔버리는 상황이 생긴다.
    # 그러므로 최대 합을 구하는 문제의 본질에 어긋남 -> 오답이다
    for i in range(len(a)):
        if a[i] < a[min_index]:
            min_index = i

    for i in range(len(b)):
        if b[i] > b[max_index]:
            max_index = i

    a[min_index], b[max_index] = b[max_index], a[min_index]
    k -= 1
    print(a)

print(sum(a))
