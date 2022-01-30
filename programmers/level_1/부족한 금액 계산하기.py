def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += i*price
    return abs(money-answer) if money-answer<0 else 0