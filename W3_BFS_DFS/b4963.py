from collections import deque
import sys
sys.setrecursionlimit(2500)
#4963. 섬의 개수
def bfs(i, j):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0
    while q:
        i, j = q.popleft()
        for k in range(8):
            ni = i + dir[k][0]
            nj = j + dir[k][1]
            if 0<=ni<h and 0<=nj<w and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                bfs(ni, nj)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
