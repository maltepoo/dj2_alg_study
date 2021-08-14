import sys

N = int(input())
rope = [int(sys.stdin.readline()) for _ in range(N)]
rope.sort()
for k in range(N):
    rope[k] = rope[k] * (N - k)
print(max(rope))