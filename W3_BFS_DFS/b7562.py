#7562. 나이트의 이동
def bfs():
    q = [(s1,s2)]
    visited[s1][s2] = 1
    while q:
        i, j = q.pop(0)
        if i == e1 and j == e2:
            return print(visited[e1][e2]-1)
        for k in range(8):
            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

T = int(input())
for tc in range(T):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    dirs = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]
    bfs()