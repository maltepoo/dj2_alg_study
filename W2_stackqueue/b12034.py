#12034. 김인천씨의 식료품가게 (Large)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    res = []
    while prices:
        p = prices.pop(0)
        if (p*100)//75 in prices:
            res.append(p)
            prices.remove((p*100)//75)
    print('Case #{}:'.format(tc), *res)

""" 시간초과
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prods = list(map(int, input().split()))
    res = []
    while len(res) <= N//2+1:
        isit = prods.pop(0)
        if int(isit*0.75) in prods:
            res.append(prods.pop(prods.index(int(isit*0.75))))
        else:
            prods.append(isit)
    print('Case #{}:'.format(tc), *res)
"""