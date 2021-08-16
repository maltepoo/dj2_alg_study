#16953. A → B
A, B = list(map(int, input().split()))
cnt = 1

while B > A and B != 1:
    if B % 10 == 1:
        B = (B-1) // 10
        cnt += 1
    elif B % 2 == 0:
        B = B // 2
        cnt += 1
    else:
        cnt = -1
        break
if A == B:
    print(cnt)
else:
    print(-1)