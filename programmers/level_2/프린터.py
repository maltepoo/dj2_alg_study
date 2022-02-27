def solution(priorities, location):
    answer = 0
    queue = [_ for _ in range(len(priorities))]
    while priorities:
        p, q = priorities.pop(0), queue.pop(0)
        if len(priorities) == 0 or p >= max(priorities):
            answer += 1
            if q == location:
                return answer
        elif p < max(priorities):
            priorities.append(p)
            queue.append(q)
    return answer