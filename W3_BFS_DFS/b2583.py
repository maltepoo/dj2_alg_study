#2583. 영역 구하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) #재귀를 사용하므로 최대 재귀 깊이를 정해주어 recursion 오류를 방지

M, N, K = map(int, input().split())
coors = [list(map(int, input().split())) for _ in range(K)]
graph = [[0]*N for _ in range(M)]

for co in coors:
    x1, y1, x2, y2 = co[0], co[1], co[2], co[3]
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def area(i, j, cnt):
    graph[i][j] = 8
    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]
        if 0 <= ni < M and 0 <= nj < N and graph[ni][nj] == 0:
            cnt = area(ni, nj, cnt+1)
    return cnt

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

cnt_list = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            cnt_list.append(area(i,j,1))
print(len(cnt_list))
print(*sorted(cnt_list))