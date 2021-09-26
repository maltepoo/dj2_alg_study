#2178. 미로 탐색
def bfs(s):
    q = [s]
    maze[s[0]][s[1]] = 1
    while q:
        i, j = q.pop(0)
        if i == N-1 and j == M-1:
            print(maze[N-1][M-1])
            break
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<M and maze[ni][nj] == 1:
                maze[ni][nj] = maze[i][j]+1
                q.append((ni,nj))

N, M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]
di = [-1, 1, 0, 0]
dj = di[::-1]
bfs((0,0))