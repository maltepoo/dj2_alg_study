#15904. UCPC는 무엇의 약자일까?
w = input()
ucpc = ['U', 'C', 'P', 'C']
i = 0
res = 'I hate UCPC'
for u in range(len(w)):
    if w[u] == ucpc[i]:
        i += 1
    if i == 4:
        break
if i > 3:
    res = 'I love UCPC'
print(res)