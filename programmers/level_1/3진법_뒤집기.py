def solution(n):
    three = ''
    q = 3
    while n > 0:
        n, mod = divmod(n, q)
        three += str(mod)
    return int(three, 3)