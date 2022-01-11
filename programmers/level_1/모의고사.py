def solution(answers):
    answer = []
    score = [0]*3
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == n1[i%5]:
            score[0] += 1
        if answers[i] == n2[i%8]:
            score[1] += 1
        if answers[i] == n3[i%10]:
            score[2] += 1
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    return answer