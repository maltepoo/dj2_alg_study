import heapq, sys
input = sys.stdin.readline
#18352. 특정 거리의 도시 찾기
def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        d, n = heapq.heappop(q)
        if dist[n] < d: continue
        for v in adjList[n]:
            new_dist = d + v[1]
            if new_dist < dist[v[0]]:
                dist[v[0]] = new_dist
                heapq.heappush(q, (new_dist, v[0]))

N, M, K, X = map(int, input().split())
adjList = [[] for _ in range(N+1)]
dist = [987654321]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    adjList[a].append((b,1))

dijkstra(X)
for d in range(len(dist)):
    if dist[d] == K:
        print(d)
if not K in dist:
    print(-1)