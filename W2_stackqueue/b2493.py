#2493. 탑
N = int(input())
h = list(map(int, input().split()))
stack = []
counter = [0]*N
for i in range(N-1, -1, -1):
    while stack:
        if stack[-1][1] <= h[i]: # stack 보다 큰 탑을 발견하면 멈춤
            counter[stack[-1][0]] = i+1 # 기록
            stack.pop() # 초기화
        else:
            break
    stack.append((i, h[i]))
print(*counter)