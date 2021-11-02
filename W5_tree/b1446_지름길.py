import sys
sys.stdin = open("input.txt")
#1446. 지름길
N, D = map(int, input().split())
hw = sorted([list(map(int, input().split())) for _ in range(N)])
dp = [ _ for _ in range(D+1)]
for i in hw:
    a, b, c = i
    if b <= D:
        dp[b] = min(dp[a]+ c, dp[b])
    for k in range(a, D+1):
        dp[k] = min(dp[k-1]+1, dp[k])
print(dp[D])