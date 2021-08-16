#13305. 주유소
C = int(input())
R = list(map(int,input().split()))
P = list(map(int,input().split()))

mp = P[0] #처음 가격 최소로 설정
res = 0
for i in range(C-1): #마지막값 제외 순회
    if mp > P[i]:
        mp = P[i]
    res += mp*R[i]
print(res)