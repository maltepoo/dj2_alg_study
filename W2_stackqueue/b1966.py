#1966. 프린터 큐
for tc in range(int(input())):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    cnt = 0

    while priority[M] != 0:
        for i in range(len(priority)):
            if priority[i] >= max(priority):
                priority[i] = 0
                cnt += 1
                if i == M:
                    print(cnt)
                    break