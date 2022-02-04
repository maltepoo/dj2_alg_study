def solution(record):
    answer = []
    user = {}
    for r in record:
        r = list(r.split())
        if r[0] == 'Enter' or r[0] == 'Change':
            user[r[1]] = r[2]
    for i in record:
        i = list(i.split())
        if i[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(user[i[1]]))
        elif i[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(user[i[1]]))
    return answer