people = int(input())
time = sorted(list(map(int,input().split())))

def small():
    res = 0

    for i in range(people):
        res += sum(time[:i+1])
    return res

print(small())

