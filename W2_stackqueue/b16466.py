#16466. 콘서트
N = int(input())
tc = sorted(list(map(int, input().split())))+[0]
cnt = 1
for i in tc:
    if cnt == i:
        cnt += 1
    else:
        print(cnt)
        break