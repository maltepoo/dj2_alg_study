from itertools import combinations
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if isPrime(sum(i)):
            answer += 1
    return answer