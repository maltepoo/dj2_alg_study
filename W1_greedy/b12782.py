T = int(input())
for tc in range(T):
    N, M = input().split()

    cnt = 0
    n1, m1 = 0, 0
    for i in range(len(N)):
        if N[i] != M[i]:
            n1 += int(N[i])
            m1 += int(M[i])
    if n1 > m1:
        print(n1)
    else:
        print(m1)
