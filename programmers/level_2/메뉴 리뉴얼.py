from itertools import combinations

menus = {}

def solution(orders, course):
    answer = []
    for i in course:
        for o in orders:
            for p in combinations(sorted(list(o)), i):
                try: menus[p] = menus[p]+1
                except: menus[p] = 1
    candies = sorted(menus.items(), key=lambda x: x[1], reverse=True)
    for c in course:
        vote = 0
        for menu in candies:
            if vote == 0:
                if len(menu[0]) == c and menu[1] > 1:
                    answer.append("".join(sorted(menu[0])))
                    vote = menu[1]
            else:
                if len(menu[0]) == c and menu[1] > 1 and vote == menu[1]:
                    answer.append("".join(sorted(menu[0])))
                else:
                    break
    return sorted(answer)