import time

start_time = time.time()

n, k = map(int, input().split())

count = 0

# 내가 작성한 답안 (반복문은 n번 만큼 쓸데없이 많이 돌게 된다.)
# for i in range(n) :
#     if n == 1:
#         break
#     elif n % k == 0:
#         n = n // k
#         count += 1
#     else:
#         n -= 1
#         count += 1


while n > 1 :
    while (n % k != 0):
        if n == 1:
            break
        n -= 1
        count += 1
        print(f"n : {n}")
    if n < k:
        continue
    n = n // k
    count += 1
    print(f"n : {n}")

print(f"count : {count}")
print((2//3) * 2)