#12605. 단어순서 뒤집기
N = int(input())
for tc in range(1, N+1):
    L = input().split()
    print('Case #{}: {}'.format(tc, " ".join(L[::-1])))