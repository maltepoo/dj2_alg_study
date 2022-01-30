def solution(n):
    answer = 9999999
    for i in range(n, 1, -1):
        mod = n % i
        if mod == 1 and i < answer:
            answer = i
    return answer