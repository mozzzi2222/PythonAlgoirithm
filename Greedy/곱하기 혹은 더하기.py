s = input()

import time

start_time = time.time()

data = []

for number in s:
    data.append(int(number))

before = 0
result = 0

for number in data:
    # 나는 before의 값까지 검사했는데 before의 값은 어차피 result에 반영되기 때문에 검사할 필요 없겠네
    # if num <= 1 or result <= 1 만 검사했으면 됐겠다
    # 하지만 그러면 위에서 인덱스 0의 값을 result에 저장해주고 시작해야함
    if (before == 0) or (number == 0) or (before == 1) or (number == 1):
        result += number
        before = number
    else :
        result *= number
        before = number

print(result)

end_time = time.time()
print(f"수행시간 : {end_time - start_time}")
