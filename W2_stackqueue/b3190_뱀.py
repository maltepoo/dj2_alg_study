#3190. 뱀
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d, sec = 1, 0 # 방향, 초
def play():
    global d, sec
    q = [(0,0)] # 뱀의 길이를 저장할 큐
    while q:
        i, j = q[-1]
        arr[i][j] = -1 # 뱀 위치 기록

        if sec in command:
            if command[sec] == 'D':
                d = (d+1)%4
            else:
                d = (d-1)%4

        ni, nj = i+dirs[d][0], j+dirs[d][1]
        if not (0<=ni<N) or not (0<=nj<N): # 하나라도 범위를 벗어나면 끝
            return sec+1
        elif arr[ni][nj] == -1: # 뱀 몸통에 닿으면 끝
            return sec+1
        if arr[ni][nj] == 1: # 사과 면
            arr[ni][nj] = -1 # 사과 없애고 뱀 기록
            q.append((ni,nj)) # 머리 붙여
        else:
            arr[ni][nj] = -1 # 경로 기록
            q.append((ni,nj)) # 머리 앞으로
            x, y = q.pop(0) # 꼬리 비우기
            arr[x][y] = 0
        sec += 1

N, K = int(input()), int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    c, r = map(int, input().split())
    arr[c-1][r-1] = 1

L = int(input())
command = {}
for _ in range(L):
    x, c = input().split()
    command[int(x)] = c
print(play())