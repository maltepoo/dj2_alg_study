def solution(n, arr1, arr2):
    answer = []
    map1, map2 = arr1, arr2
    for i in range(n):
        answer.append(bin(map1[i] | map2[i])[2:].zfill(n).replace('1', '#').replace('0', ' '))
    return answer