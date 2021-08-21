#12605. 단어순서 뒤집기
N = int(input())
for tc in range(1, N+1):
    #일반풀이
    L = input().split()
    print('Case #{}: {}'.format(tc, " ".join(L[::-1])))

    #스택풀이
    L = input().split()
    stack = []
    for l in L:
        stack.append(l)
    print("Case #{}:".format(tc), end=" ")
    for _ in range(len(stack)):
        print(stack.pop(), end=" ")
    print()