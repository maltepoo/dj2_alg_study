#2606. 바이러스
def dfs(C):
    s = 1
    visited = [0]*(C+1)
    stack = [s]
    visited[s] = 1
    i = s
    cnt = 0
    while i != 0:
        for w in range(1, C+1):
            if adj[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[w] = 1
                cnt += 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0
    return cnt

C = int(input())
net = int(input())
adj = [[0]*(C+1) for _ in range(C+1)]
for _ in range(net):
    V, E = map(int, input().split())
    adj[V][E] = 1
    adj[E][V] = 1

print(dfs(C))
