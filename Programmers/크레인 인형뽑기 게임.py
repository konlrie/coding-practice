def solution(board, moves):
    answer = []
    result = 0
    for i in moves:
        for j in range(len(board)):
            check = board[j][i-1]
            if len(answer) == 0:
                if check != 0:
                    answer.append(check)
                    board[j][i-1] = 0
                    break
            else:
                if check != 0 and check != answer[-1]:
                    answer.append(check)
                    board[j][i-1] = 0
                    break
                elif check == answer[-1]:
                    answer.pop()
                    board[j][i-1] = 0
                    result += 2
                    break
    return result

test_board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
test_moves = [1,5,3,5,1,2,1,4]
print(solution(test_board, test_moves))