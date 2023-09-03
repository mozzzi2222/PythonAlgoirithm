import time
import itertools

n = int(input()) # 모험가 수 입력
fear = list(map(int, input().split())) #공포도 입력

start_time = time.time()

# 오름차순으로 정렬
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

