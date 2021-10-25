#1189. 컴백홈
def bt(start, dist):
    global res
    i, j = start
    if dist == K and arr[i][j] == 'H':
        res += 1
        return
    for k in range(4):
        ni, nj = i+dirs[k][0], j+dirs[k][1]
        if 0<=ni<R and 0<=nj<C and visited[ni][nj] == 0 and arr[ni][nj] != 'T':
            visited[ni][nj] = 1
            bt((ni,nj), dist+1)
            visited[ni][nj] = 0

R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
dirs = [(0,-1), (0,1), (-1,0), (1, 0)]
arr[0][C-1] = 'H'
res = 0
visited[R-1][0] = 1
bt((R-1,0),1)
print(res)