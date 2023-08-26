s = input()

import time

start_time = time.time()

data = []

for number in s:
    data.append(int(number))

before = 0
result = 0

for number in data:
    if (before == 0) or (number == 0) or (before == 1) or (number == 1):
        result += number
        before = number
    else :
        result *= number
        before = number

print(result)

end_time = time.time()
print(f"수행시간 : {end_time - start_time}")
