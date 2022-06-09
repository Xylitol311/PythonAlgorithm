def solution(board, moves):
    basket = []
    answer = 0
    for doll in moves:
        for loc in board:
            if loc[doll - 1] != 0:
                basket.append(loc[doll - 1])
                if len(basket) >= 2 and basket[-1] == basket[-2]:
                    answer += 1
                    del basket[-2:]
                loc[doll - 1] = 0
                break
    return answer * 2

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
