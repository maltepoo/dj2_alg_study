#11497. 통나무 건너뛰기
T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()

    cnt = [abs(L[0]-L[1])] #abs(L[-1]-L[-2])도 추가해야 할 듯
    for i in range(N-2):
        cnt.append(abs(L[i]-L[i+2]))
    print(max(cnt))