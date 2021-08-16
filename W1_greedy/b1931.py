#1931. 회의실 배정
import sys
input = sys.stdin.readline
N = int(input())
mt = [list(map(int, input().split())) for _ in range(N)]

mt.sort(key=lambda x: (x[1], x[0]))
find = mt[0][1]
cnt = 1
for i in range(1, N):
    if mt[i][0] >= find:
        find = mt[i][1]
        cnt += 1
print(cnt)

#시간초과
# N = int(input())
# mt = [list(map(int, input().split())) for _ in range(N)]
# res = []
# for j in range(N):
#     find = mt[j][1]
#     cnt = 1
#     for i in range(1, N):
#         if mt[i][0] >= find:
#             find = mt[i][1]
#             cnt += 1
#     res.append(cnt)
# print(max(res))