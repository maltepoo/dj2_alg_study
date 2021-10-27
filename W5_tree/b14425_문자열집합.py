import sys
input = sys.stdin.readline
#14425. 문자열 집합
N, M = map(int,input().split())
origin = [input() for _ in range(N)]
cnt = 0
for _ in range(M):
    ip = input()
    if ip in origin:
        cnt += 1
        origin.remove(ip)
print(cnt)
"""
list로의 확인은 O(N)이지만
dict는 O(1)이므로 dict가 더 효율적
"""
N, M = map(int,input().split())
origin = {input() for _ in range(N)} # 자료 구조만 바꿈!!
cnt = 0
for _ in range(M):
    ip = input()
    if ip in origin:
        cnt += 1
print(cnt)