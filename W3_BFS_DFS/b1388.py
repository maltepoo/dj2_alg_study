#1388. 바닥 장식
N, M = map(int,input().split()) #세로 N 가로 M
board = [list(input()) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == '-':
            board[i][j] = '■'
            if j == (M-1) or board[i][j+1] == '|':
                cnt += 1

for i in range(M):
    for j in range(N):
        if board[j][i] == '|':
            board[j][i] = '□'
            if j == (N-1) or board[j+1][i] == '-' or board[j+1][i] == '■':
                cnt += 1
print(cnt)