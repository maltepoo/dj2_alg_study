N, K = map(int, input().split())
coins = []
cnt = 0

for i in range(N):
    coins.append(int(input()))
for j in range(1,len(coins)+1):
    cnt += K // coins[-j]
    K %= coins[-j]

print(cnt)