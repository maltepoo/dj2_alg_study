def solution(s, n):
    answer = ''
    for i in s:
        if 65 <= ord(i) <= 90:
            answer += chr(65 + (ord(i) + n - 65) % 26)
        elif 97 <= ord(i) <= 122:
            answer += chr(97 + (ord(i) + n - 97) % 26)
        else:
            answer += " "
    return answer