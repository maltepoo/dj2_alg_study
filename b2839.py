#풀이 1
sugar = int(input())
cnt = 0

while sugar >= 0:
    if sugar % 5 == 0:
        cnt += (sugar // 5)
        print(cnt)
        break
    sugar -= 3
    cnt += 1
else:
    print('-1')

#풀이 2
n = int(input())
a = n // 5
b = n // 3
li = []

for i in range(a,-1,-1):
    for j in range(0,b+1,1):
        if n == 5*i+3*j:
            li.append(i+j)
if li == []:
    print('-1')
else:
    print(min(li))