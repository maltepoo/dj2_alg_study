n = input()
minus = n.split("-")
tot = []

for m in minus:
    tot.append(sum(list(map(int,m.split('+')))))
res = tot[0]
for t in tot[1:]:
    res = res - t
    
print(res)