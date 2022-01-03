def solution(numbers, hand):
    answer = ''
    L, R = 10, 12
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            L = i
        elif i in [3, 6, 9]:
            answer += 'R'
            R = i
        else:
            if i == 0: i = 11
            if sum(divmod(abs(L - i), 3)) > sum(divmod(abs(R - i), 3)):
                answer += 'R'
                R = i
            elif sum(divmod(abs(L - i), 3)) < sum(divmod(abs(R - i), 3)):
                answer += 'L'
                L = i
            else:
                if hand == 'right':
                    answer += 'R'
                    R = i
                else:
                    answer += 'L'
                    L = i
    return answer