#5585. 거스름돈
n = 1000 - int(input())
cnt = 0
array = [500, 100, 50, 10, 5, 1]
for coin in array:
    cnt += n // coin
    n %= coin

print(cnt)