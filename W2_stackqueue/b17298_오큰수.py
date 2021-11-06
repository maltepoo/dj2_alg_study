#17298. 오큰수
N = int(input())
As = list(map(int, input().split()))
res, stack = [-1]*N, [0]
for i in range(1, N):
    while stack and As[stack[-1]] < As[i]:
        # stack을 인덱스만 저장하는 용도로 씀
        res[stack.pop()] = As[i]
    stack.append(i)
print(*res)

"""
시간초과 날듯
N = int(input())
As = list(map(int, input().split()))
res = []
for i in range(N):
    for j in range(i, N):
        if As[i] < As[j]:
            res.append(As[j])
            break
    if len(res) != (i+1):
        res.append(-1)
print(*res)
"""