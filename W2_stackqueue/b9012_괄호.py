#9012. 괄호
T = int(input())
for _ in range(T):
    vps = input()
    n = [vps[0]]
    for i in range(1, len(vps)):
        if n:
            if vps[i] == n[-1]:
                n.append(vps[i])
            else:
                if vps[i] == '(' and n[-1] == ')':
                    n.append(vps[i])
                else: n.pop()
        else: n.append(vps[i])
    if n: print('NO')
    else: print('YES')