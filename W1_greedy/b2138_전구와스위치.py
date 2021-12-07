import copy
#2138. 전구와 스위치
def swichOn(s, c):
    cnt = c
    for i in range(1, N):
        if s[i-1] != g[i-1]:
            swich(i-1, i+1, s)
            cnt += 1
    return cnt if s == g else -1

def swich(a, b, s):
    for i in range(a, b+1):
        if 0<=i< N:
            if s[i] == 1:
                s[i] = 0
            else:
                s[i] = 1

N = int(input())
s, g = list(map(int, input())), list(map(int, input()))
res = 0

s1 = copy.deepcopy(s)
first = swichOn(s, 0)

swich(0, 1, s1) # 0번 스위치를 바꿔 줌
second = swichOn(s1, 1)

if first != -1 and second != -1:
    res = min(first, second)
elif first == -1 and second == -1:
    res = -1
else:
    res = max(first, second)
print(res)