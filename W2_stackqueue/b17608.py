#17608. 막대기
N = int(input())
bar = [int(input()) for _ in range(N)]
cnt = 1
bg = bar[-1]
for b in bar[::-1]:
  if b > bg:
      cnt += 1
      bg = b
print(cnt)
