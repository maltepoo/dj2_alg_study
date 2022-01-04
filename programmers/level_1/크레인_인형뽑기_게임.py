def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        m = m-1
        for i in range(len(board)):
            if board[i][m] != 0:
                if stack and stack[-1] == board[i][m]:
                    board[i][m] = 0
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][m])
                    board[i][m] = 0
                break
    return answer