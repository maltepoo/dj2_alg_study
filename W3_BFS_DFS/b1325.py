from collections import deque
import sys
input = sys.stdin.readline
#1325. 효율적인 해킹
def bfs(n):
    cnt = 1
    q = deque([adj[n-1]])
    visited = [0]*(N+1)
    visited[n] = 1
    while q:
        p = q.popleft()
        for i in p:
            if not visited[i]:
                q.append(adj[i-1])
                visited[i] = 1
                cnt += 1
    return cnt

N, M = map(int,input().split())
adj = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    adj[B-1].append(A)

res = []
maxV = 0
for i in range(1, N+1):
    cnt = bfs(i)
    if cnt > maxV:
        maxV = cnt
    res.append((i, cnt))
for j, cnt in res:
    if cnt == maxV:
        print(j, end=" ")