n = int(input())

coin_type = [500, 100, 50, 10]
count = 0

# coin_type 만큼 반복 ( 금액 n과는 관계없이 화폐의 종류만큼만 반복한다,)
# O(K)의 시간 복잡도를 보장
for coin in coin_type :
    count += n // coin
    n = n % coin

print(count)