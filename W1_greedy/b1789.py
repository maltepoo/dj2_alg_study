n = int(input())
plus = 0
li = []

for i in range(1,n+1):
    plus += i
    li.append(i)
    if plus == n:
        print(len(li))
        break
    elif plus > n:
        print(len(li)-1)
        break