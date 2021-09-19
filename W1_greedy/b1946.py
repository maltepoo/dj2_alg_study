#1946. 신입 사원
T = int(input())
for tc in range(T):
    N = int(input())
    arr = sorted([list(map(int, input().split())) for _ in range(N)])
    mx = arr[0][1]
    cnt = 1
    for i in range(1, N):
        if arr[i][1] < mx:
            cnt += 1
            mx = arr[i][1]
    print(cnt)