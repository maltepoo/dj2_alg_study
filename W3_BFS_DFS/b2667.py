from collections import deque
#2667. 단지번호붙이기
N = int(input())
graph = [list(map(int,input())) for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 1

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i+dy[k]
            nj = j+dx[k]
            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] == 1:
                    graph[ni][nj] = 0
                    q.append((ni,nj))
                    cnt += 1
    return cnt

houses = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append(bfs(i,j))
print(len(houses))
for i in sorted(houses):
    print(i)