#1874. 스택 수열
import sys
input = sys.stdin.readline

n = int(input())
ns = [int(input()) for _ in range(n)]

i = 1
idx = 0
flag = True
stack, res = [], []

while idx < n:
    if idx == n:
        break
    if stack and stack[-1] == ns[idx]:
        stack.pop()
        res.append('-')
        idx += 1
    elif i > ns[idx]:
        flag = False
        break
    else:
        stack.append(i)
        res.append('+')
        i += 1

if flag:
    for j in res:
        print(j)
else:
    print('NO')
