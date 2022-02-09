import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville:
        p = heapq.heappop(scoville)
        if p >= K:
            return answer
        if len(scoville) >= 1:
            heapq.heappush(scoville, p+heapq.heappop(scoville)*2)
            answer += 1
        else: return -1
    return answer