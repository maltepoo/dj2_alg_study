#18429.근손실
def backtracking(power, day):
    global cnt
    if day == N:
        cnt += 1
        return
    for i in range(N):
        if used[i] == 0 and power+kit[i] >= 500:
            used[i] = 1
            backtracking(power+kit[i], day+1)
            used[i] = 0

N, K = map(int, input().split())
kit = list(map(lambda x:x-K, map(int, input().split())))
used, cnt = [0]*(N), 0
backtracking(500,0)
print(cnt)