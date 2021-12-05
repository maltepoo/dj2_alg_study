#1246. 온라인 판매
N, M = map(int,input().split())
deal = [int(input()) for _ in range(M)]
deal.sort()
idx, res = 0, 0
if N > M: start = -M
else: start = -N
for i in range(len(deal[start:])):
    p = deal[start:][i]
    many = deal[start:][i] * len(deal[start:][i:])
    if many > res:
        idx, res = p, many
print(idx, res)