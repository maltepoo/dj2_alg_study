def solution(nums):
    how = len(nums) // 2
    set_nums = set(nums)
    if how <= len(set_nums):
        return how
    else:
        return len(set_nums)