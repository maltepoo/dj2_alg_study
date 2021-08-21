#2164. 카드2
import collections
deq = collections.deque([_ for _ in range(int(input()),0,-1)])
while len(deq)>1:
    deq.pop()
    deq.appendleft(deq.pop())
print(*deq)

# readline 써도 시간초과(시간복잡도)
# N = int(input())
# stack = [_ for _ in range(N,0,-1)]
# while len(stack) > 1:
#     stack.pop()
#     stack.insert(0,stack.pop())
# print(*stack)