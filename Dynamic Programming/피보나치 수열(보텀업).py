d = [0]*100

d[1] = 1
d[2] = 1
n = 99
# 피보나치 함수를 반복문으로 구현
for i in range(3, n + 1):
    d[i] = d[i -1] + d[i - 2]

print(d[n])