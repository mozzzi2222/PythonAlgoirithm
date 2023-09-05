import time

data = input()


# 시간측정
start_time = time.time()

number = [1, 2, 3, 4, 5, 6, 7, 8]
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = 0
y = int(data[1])

for i in range(len(alphabets)):
    if data[0] == alphabets[i]:
        x = number[i]

print(f"처음 입력받은 값 정수로 변환 {x} {y}")

move_types = ['ul', 'ur', 'ru', 'rd', 'dr', 'dl', 'ld', 'lu' ]
mx = [-1, 1, 2, 2, 1, -1, -2, -2]
my = [-2, -2, -1, 1, 2, 2, 1, -1]

count = 0
for i in range(len(move_types)):
    nx = x + mx[i]
    ny = y + my[i]

    print(f"각 무브타입마다 xy값 {nx} {ny}")
    if nx > 0 and ny > 0:
        count += 1

print(count)
end_time = time.time()
print(end_time - start_time)
