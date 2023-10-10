n = int(input())

d = [0] * 1001

data = [(1,2), (2, 1), (2, 2)]
d[0] = 0
d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-1] + 2 * d[i-2]

print(d[n])