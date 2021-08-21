#10773. 제로
K = int(input())
arr = [int(input()) for _ in range(K)]
stack = []
ans = 0
for i in arr:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()
if True:
    for i in stack:
        ans+=i
    print(ans)