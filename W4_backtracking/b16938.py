#16938. 캠프 준비
n, l, r, x = map(int, input().split())
lev = list(map(int, input().split()))
cnt = 0
for i in range(1, 1<<n):
    res = []
    for j in range(0, n):
        if i & (1 << j):
            res.append(lev[j])
    if l <= sum(res) <= r and max(res)-min(res) >= x:
        cnt += 1
print(cnt)