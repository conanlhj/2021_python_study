def isEnd():
    for i in board:
        if 0 in i:
            return True
    # for문이 중간에 return으로 끊기지 않았다면, 모든 타일이 숫자로 차있다.
    return False


def removePossibles_line(b_line, p_line):
    # 현재 사용되고 있는 숫자 정렬 후 0제외
    removes = sorted(set(b_line))[1:]
    # p_line안에서.
    for i in p_line:
        # 가능성이 1개 이상일 때
        if len(i) > 1:
            # 숫자들을 제외할건데
            for j in removes:
                # 이미 가능성에 없으면 pass
                if j in i:
                    i.remove(j)
    return p_line


def printBoard():
    for i in range(9):
        for j in range(9):
            if (board[i][j]):  # 숫자 있으면 숫자 출력 없으면 □출력
                print(board[i][j], end=' ')
            else:
                print("□", end=' ')
        print()
    print()


# 보드판 만들기
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# possibles라는 list 만들고
possibles = []
# 각 행마다
for i in range(9):
    possibles.append([])  # 빈 list 추가
    for j in range(9):  # 각 열마다
        if board[i][j]:  # 해당 타일에 이미 숫자가 있으면.
            # 숫자를 리스트에 집어넣고 그걸 추가. i = j = 0인 경우에 [5]를 추가
            possibles[i].append([board[i][j]])
        else:
            # [1, 2, 3, 4, ..., 9] 추가
            possibles[i].append([_ for _ in range(1, 10)])
printBoard()
removePossibles_line(board[0], possibles[0])
