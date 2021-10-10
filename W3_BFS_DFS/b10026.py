import sys
sys.setrecursionlimit(10000)
#10026. 적록색약
def RGB(i, j, flag):
    global cnt
    v1[i][j] = 1
    for k in range(4):
        ni, nj = i+dir[k][0], j+dir[k][1]
        if 0<=ni<N and 0<=nj<N and flag == arr[ni][nj] and v1[ni][nj] == 0:
            RGB(ni, nj, flag)

def RGnB(i, j, flag):
    global rcnt
    arr[i][j] = 0
    color = flag
    for k in range(4):
        ni, nj = i + dir[k][0], j + dir[k][1]
        if 0 <= ni < N and 0 <= nj < N:
            if color == 'R':
                if arr[ni][nj] == 'R' or arr[ni][nj] == 'G':
                    RGnB(ni, nj, color)
            elif color == 'G':
                if arr[ni][nj] == 'R' or arr[ni][nj] == 'G':
                    RGnB(ni, nj, color)
            else:
                if flag == arr[ni][nj]:
                    RGnB(ni, nj, color)

N = int(input())
arr = [list(input()) for _ in range(N)]
v1 = [[0]*N for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt, rcnt = 0, 0

for i in range(N):
    for j in range(N):
        if v1[i][j] == 0:
            RGB(i, j, arr[i][j])
            cnt += 1
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            RGnB(i, j, arr[i][j])
            rcnt += 1
print(cnt, rcnt)