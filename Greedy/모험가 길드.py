import time
import itertools

n = int(input())
fear = list(map(int, input().split()))

start_time = time.time()

data = sorted(fear)

result = 0
count = 1
print(data)
# 소스코드
for i in data:
    if i <= count:
        count = 1
        result += 1
    else:
        count += 1


print(result)

end_time = time.time()
print(f"수행시간 : {end_time - start_time}")

