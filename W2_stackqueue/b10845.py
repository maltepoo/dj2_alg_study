#10845. 큐
N = int(input())
b = []
for _ in range(N):
    order = input()
    if 'push' in order:
        o, n = map(str, order.split())
        b.append(n)
    if 'pop' in order:
        if not len(b):  # 0이면
            print(-1)
        else:
            print(b.pop(0))
    if 'size' in order:
        print(len(b))
    if 'empty' in order:
        if not len(b):
            print(1)
        else:
            print(0)
    if 'front' in order:
        if not len(b):
            print(-1)
        else:
            print(b[0])
    if 'back' in order:
        if not len(b):
            print(-1)
        else:
            print(b[-1])