from collections import deque
#1697. 숨바꼭질
def bfs():
    q = deque()
    q.append(N)
    while q:
        p = q.popleft()
        if p == K:
            print(res[p])
            break
        for loc in (p-1, p+1, p*2):
            if 0 <= loc <= 100000 and not res[loc]:
                res[loc] = res[p]+1
                q.append(loc)

N, K = map(int, input().split())
res = [0]*100001
bfs()