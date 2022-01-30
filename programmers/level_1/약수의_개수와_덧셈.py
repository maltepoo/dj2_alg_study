def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        measure = set()
        for j in range(1,i+1):
            if i%j == 0:
                measure.add(j)
                measure.add(i//j)
        if len(measure) % 2:
            answer -= i
        elif len(measure) <= 0:
            continue
        else: answer += i
    return answer
print(solution(1, 2))