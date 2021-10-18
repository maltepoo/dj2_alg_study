#1700. 멀티탭 스케줄링
n, k = map(int, input().split())
elec = list(map(int, input().split()))
tab = []
cnt = 0
for i in range(k):
    if elec[i] in tab:
        continue
    elif not elec[i] in tab and len(tab)<n:
        tab.append(elec[i])
    else:
        item, plug = 0, 0
        for m in tab:
            if m not in elec[i:]:
                item = m
                break
            else:
                idx = elec[i:].index(m)
                if idx > plug:
                    plug = idx
                    item = m
        tab.remove(item)
        tab.append(elec[i])
        cnt += 1
print(cnt)