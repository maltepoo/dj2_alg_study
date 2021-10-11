#2239. 스도쿠
def possible(i, j):
    possible_num = [1 for _ in range(10)]
    # 가로체크
    for r in range(9):
        if arr[i][r] != 0:
            possible_num[arr[i][r]] = 0
    # 세로체크
    for c in range(9):
        if arr[c][j] != 0:
            possible_num[arr[c][j]] = 0
    # 3x3체크
    for t in range(3):
        for h in range(3):
            possible_num[arr[(i//3)*3 + t][(j//3)*3 + h]] = 0
    return possible_num

def fill_num(idx):
    global path
    if idx == len(path):
        for p in range(9):
            print(*arr[p], sep="")
        exit()

    ni, nj = path[idx][0], path[idx][1]
    possibles = possible(ni, nj)
    for i in range(1, 10):
        if possibles[i]: # True
            arr[ni][nj] = i
            fill_num(idx+1)
            arr[ni][nj] = 0

arr = [list(map(int, input())) for _ in range(9)]
path = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            path.append((i,j))
fill_num(0)