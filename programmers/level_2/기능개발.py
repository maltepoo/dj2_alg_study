import math

def solution(prog, speeds):
    answer = []
    idx, cnt = 0, 1
    while prog:
        n = math.ceil((100-prog.pop(0))/speeds.pop(0))
        while prog:
            if prog[idx]+(n*speeds[idx]) >= 100:
                prog.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
                break
    answer.append(cnt)
    return answer