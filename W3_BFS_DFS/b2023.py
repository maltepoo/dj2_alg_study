#2023. 신기한 소수
"""
소수란 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수
"""
def check(num):
    for i in range(2, int(int(num)**0.5)+1):
        if int(num) % i == 0:
            return
    if len(num) == n:
        print(num)
        return
    for p in prime:
        check(num+p)

n = int(input())
start = ['2', '3', '5', '7']
prime = ['1', '3', '7', '9']
for s in start:
    check(s)