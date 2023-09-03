n, k = map(int, input().split())

count = 0
# 모범 답안 : n이나 k가 아무리 커져도 log(k)의 시간 복잡도를 보장
while True:
    # n이 k로 나누어 떨어지지 않는다고 할 때 n에서 가장 가장 가까운 수 중 k로 나누어 떨어지는 수를 찾음
    target = (n // k) * k
    count += (n - target)
    # 반드시 count를 먼저 세준 다음에 n을 target으로 바꿔주어야 함
    n = target
    # n이 k보다 작아지면 n//k가 0이 되기 때문에 반복문 탈출
    if n < k:
        break
    n //= k
    count += 1

# n < k가 되면 반복문을 빠져나와서 target과 같은 원리로 1이 될 때 까지의 count 세기 ( 1 == n - count 의 원리 )
count += (n - 1)

# 답안 출력
print(count)
