import time

# n, k 입력
n, k = map(int, input().split())

start_time = time.time()

count = 0

# 내가 작성한 답안 (반복문은 n번 만큼 쓸데없이 많이 돌게 된다.)
for i in range(n) :
    # n이 1이 되면 반복문 탈출
    if n == 1:
        break
    # n이 k로 나누어 떨어지게 되면 나누고 count++
    elif n % k == 0:
        n = n // k
        count += 1
    # 그 이외 상황은 1을 빼고 count++
    else:
        n -= 1
        count += 1

# 수정 답안
## n이 1보다 클때는 무조건 반복
# while n > 1 :
## 반복문 안에서 n이 k로 나누어 떨어지지 않는다면 1을 빼주는 과정 계속 반복
#     while (n % k != 0):
#         if n == 1:
#             break
#         n -= 1
#         count += 1
#         print(f"n : {n}")
## n이 k보다 작아지면 반복문 처음으로 돌아가기
#     if n < k:
#         continue
## 그 이외의 상황(n이 k로 나누어 떨어질 때)은 n을 k로 나누어 줌
#     n = n // k
#     count += 1
#     print(f"n : {n}")

print(f"count : {count}")
