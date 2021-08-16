#17609. 회문
def is_palin(left, right, check):
    res = check
    while (left < right):
        if word[left] != word[right] and check == 0:
            c1 = is_palin(left+1, right, check+1)
            c2 = is_palin(left, right-1, check+1)
            res = min(c1,c2)
            return res
        elif word[left] != word[right] and check == 1:
            return 2
        else:
            left += 1
            right -= 1
    return res

T = int(input())
for _ in range(T):
    word = input()
    print(is_palin(0,len(word)-1,0))

# 시간초과
T = int(input())
for tc in range(1, T+1):
    word = []
    check = []
    w = word.extend(input())
    cnt = 0

    if word == word[::-1]:
        cnt -= 1
    else:
        for i in range(len(word)):
            check = word[i]
            word.pop(i)
            if word == word[::-1]:
                cnt += 1
                break
            else:
                word.insert(i, check)
    if cnt == 0:
        print(2)
    elif cnt < 0:
        print(0)
    else:
        print(1)