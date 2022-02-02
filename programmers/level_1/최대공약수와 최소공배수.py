def solution(n, m):
    x, i = max(n, m), min(n, m)
    cnt = 1
    while cnt > 0:
        cnt = x % i
        x, i = i, cnt
    answer = [x, int(n*m/x)]
    return answer