def solution(board, moves):
    answer = 0
    lines = list(map(list, list(zip(*board))))
    for r in lines:
        while 0 in r:
            r.remove(0)
    stack = []
    for move in moves:
        try:
            stack.append(lines[move-1].pop(0))
            if stack[-1] == stack[-2]:
                answer += 2
                stack.pop()
                stack.pop()
        except IndexError:
            pass
    return answer


print(solution([[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
