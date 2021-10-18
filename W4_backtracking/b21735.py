#21735. 눈덩이 굴리기
N, M = map(int, input().split())
rand = list(map(int, input().split()))
max_ball = 0
def dfs(sec, snowball, loc):
    global max_ball
    if loc == N-1 or sec == M:
        if max_ball < snowball:
            max_ball = snowball
    else:
        if loc+1 < N:
            dfs(sec+1, snowball+rand[loc+1], loc+1)
        if loc+2 < N:
            dfs(sec+1, snowball//2+rand[loc+2], loc+2)
    return max_ball
print(dfs(0, 1, -1))