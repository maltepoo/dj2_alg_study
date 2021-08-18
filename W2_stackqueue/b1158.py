#1158. 요세푸스 문제
N, K = map(int,input().split())
y = [ _ for _ in range(1,N+1)]
ny = []
idx = K - 1
while len(y) > 0:
    if idx >= len(y):
        idx = idx % len(y)
        ny.append(y.pop(idx))
        idx += K - 1
    else:
        ny.append(y.pop(idx))
        idx += K - 1
print("".join(str(ny)).replace('[','<').replace(']','>'))