#1182. 부분수열의 합
def bt(idx, tot):
    global cnt
    if idx >= N:
        return
    if tot + nums[idx] == S:
        cnt += 1
    bt(idx+1, tot)
    bt(idx+1, tot+nums[idx])

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
bt(0,0)
print(cnt)
