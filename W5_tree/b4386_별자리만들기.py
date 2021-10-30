import sys
sys.stdin = open("input.txt")
#4386. 별자리 만들기
def find(x):
    if parent[x] == x:
        return x
    else: return find(parent[x])

def union(x, y):
    if find(y) == find(x):
        return
    parent[find(y)] = find(x)

N = int(input())
stars = [tuple(map(float, input().split())) for _ in range(N)]
edges = [] # 가중치와 x, y 위치를 저장 할 배열
parent = [_ for _ in range(N)]

for i in range(N-1): # 모든 별들과의 각각 거리 계산
    for j in range(i+1, N):
        d = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** 0.5
        edges.append((d, i, j))
edges.sort() # 정렬 하면 맨 앞 값을 기준으로 정렬(lambda 쓸 필요 x)
print(edges)
res = 0
# while edges:
#     p = edges.pop()
#     cost, x, y = p
#     if find(x) != find(y):
#         union(x, y)
#         res += cost

for cost, x, y in edges:
    if find(x) != find(y):
        union(x, y)
        res += cost
print('{:.2f}'.format(res))
