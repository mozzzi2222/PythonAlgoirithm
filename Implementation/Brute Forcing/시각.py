import time

# 정수 N(시간)입력
n = int(input())

# 시간 측정
start_time = time.time()


# 소스 코드
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 해당 조건문에서 모든 상황에서의 3의 개수 가능
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

print(str(1)+str(2)+str(3))

end_time = time.time()
print(f"수행시간 : {end_time - start_time}")
