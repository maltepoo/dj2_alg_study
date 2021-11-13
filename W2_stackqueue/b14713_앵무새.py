#14713. 앵무새
N = int(input())
cnt, tcnt = 0, 0
log = [0]*N
word = []

for _ in range(N):
    temp = input().split()
    cnt += len(temp)
    word.append(temp)
sent = input().split()

while sent:
    p = sent.pop(0)
    tcnt += 1
    for j in range(N):
        flag = False
        if log[j] <= len(word[j])-1 and p == word[j][log[j]]:
            log[j] += 1
            flag = True
            break
        if j == (N-1) and flag == False:
            print('Impossible')
            exit(0)

if sent or cnt != tcnt:
    print('Impossible')
else:
    print('Possible')