#15500. 이상한 하노이의 탑
N = int(input())
ai = list(input().split())
cnt, mv = 0, N
s2, s3, seq = [], [], []
while True:
    if len(s3) == N and s3[-1] == '1':
        break
    if ai:
        while ai:
            s = ai.pop(-1)
            if s != str(mv):
                s2.append(s)
                seq.append("1 2")
                cnt += 1
            elif s == str(mv):
                s3.append(s)
                seq.append("1 3")
                cnt += 1
                mv -= 1
    elif s2:
        while s2:
            s = s2.pop(-1)
            if s != str(mv):
                ai.append(s)
                seq.append("2 1")
                cnt += 1
            elif s == str(mv):
                s3.append(s)
                seq.append("2 3")
                cnt += 1
                mv -= 1
print(cnt)
for i in seq:
    print(i)