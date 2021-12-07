#1026. 보물
N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = list(map(int, input().split()))
res = 0
for i in range(N):
    res += A[i]*min(B)
    B.pop(B.index(min(B)))
print(res)