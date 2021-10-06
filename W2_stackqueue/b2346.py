#2346. 풍선 터뜨리기
N = int(input())
q = list(map(int, input().split()))
qidx = [_ for _ in range(1, N+1)]
res = []

idx = 0
i = q.pop(0)
res.append(qidx.pop(idx))
while q:
    if i < 0:
        idx = (i+idx) % len(q)
    else:
        idx = ((i-1)+idx) % len(q)
    i = q.pop(idx)
    res.append(qidx.pop(idx))
print(*res)