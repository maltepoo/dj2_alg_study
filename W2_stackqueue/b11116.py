#11116. 교통량
N = int(input())
for tc in range(1, N+1):
    m = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    cnt = 0
    for i in range(m):
        if (left[i] + 500) in left and (left[i] + 1000) in right and (left[i] + 1500) in right:
            cnt += 1
    print(cnt)

