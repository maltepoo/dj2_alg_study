#2644. 촌수계산
n = int(input())
s, e = map(int, input().split())
m = int(input())
adjList = [[]*(n+1) for _ in range(n+1)]
visit = [-1]*(n+1)
for _ in range(m):
    n1, n2 = map(int, input().split())
    adjList[n1].append(n2)
    adjList[n2].append(n1)

def bfs(s, e):
    q = [s]
    visit[s] = 0
    while q:
        p = q.pop()
        for w in adjList[p]:
            if visit[w] == -1:
                q.append(w)
                visit[w] = visit[p] + 1
            if w == e:
                return visit[w]
    return -1
print(bfs(s,e))