from collections import deque
#1012. 유기농 배추
def bfs(x, y):
    q = deque()
    q.append((x,y))
    arr[y][x] = 0
    while q:
        j, i = q.popleft()
        for k in range(4):
            nj = j+dir[k][1]
            ni = i+dir[k][0]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    q.append((nj,ni))

for tc in range(1, int(input())+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(K):
        x, y = map(int,input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                """
                한번 bfs를 돌면 인접한 영역의 1을
                모두 0으로 만들어버려 cnt 수만 세면
                영역의 개수가 나온다
                """
                bfs(j, i)
                cnt += 1
    print(cnt)

