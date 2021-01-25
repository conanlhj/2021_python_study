# 가능성 지워주는 함수
def removePossibles_line(b_line, p_line):
    # p_line에서 지워야 하는 숫자가 무엇인지를 removes에 넣음
    removes = sorted(set(b_line))[1:]
    # p_line에서 한 칸에 있는 가능성들마다.
    for i in p_line:
        # 확정된 칸(가능성이 하나만 남은 경우)이 아닌 경우에
        if len(i) > 1:
            # removes에 있는 지워야 되는 것들을 가져와서
            for j in removes:
                # 만약 지워야 하는 숫자가 해당 칸의 가능성에 남아있으면
                if j in i:
                    # 지운다.
                    i.remove(j)
    return p_line


# possibles를 보고, 가능성이 하나 남으면, board에 적용시켜야한다.
def apply_possible():
    # 모든 요소에서 (2중for문)
    for i in range(9):
        for j in range(9):
            # possibles의 길이가 1이면
            if len(possibles[i][j]) == 1:
                # board에 적용
                board[i][j] = possibles[i][j][0]


# 박스를 한줄로 만들어서 푸는 함수.
def line_box():
    for i in range(9):  # i -> 박스 한 칸마다.
        line = []       # board에서 박스를 한 줄로 받아옴
        l_possibles = []    # possibles에서 마찬가지.
        for j in range(9):  # 박스 안에 9개의 요소들
            y = j // 3 + (i // 3) * 3   # x좌표와 y좌표는 다음과 같이 설정하면 박스 하나씩
            x = j % 3 + (i % 3) * 3
            line.append(board[y][x])    # line과 l_possibles 만들기.
            l_possibles.append(possibles[y][x])
        l_possibles = removePossibles_line(line, l_possibles)   # l_possibles갱신
        for j in range(9):  # possibles에 적용
            possibles[y][x] = l_possibles[j]
        apply_possible()    # board에 쓸 게 있는지 확인


# 가로줄 만들어서 푸는 함수.
def line_horizontal():
    for i in range(9):  # 모든 가로줄마다.
        removePossibles_line(board[i], possibles[i])  # 가로줄 보내고
    apply_possible()  # 바로 적용


# 세로줄 만들어서 푸는 함수.
def line_vertical():
    for i in range(9):  # i -> 세로.
        line = []       # board에서 세로줄 받아올 리스트.
        l_possibles = []    # possibles에서 세로줄 받아올 리스트.
        for j in range(9):  # j -> 가로.
            line.append(board[j][i])    # [j][i] 가로 세로 위치 바꿔서 세로줄을 한 줄로 가져옴.
            l_possibles.append(possibles[j][i])  # 마찬가지
        l_possibles = removePossibles_line(line, l_possibles)  # removePossibles_line에서 l_possibles갱신
        for j in range(9):
            possibles[j][i] = l_possibles[j]  # possibles 갱신.
    apply_possible()  # 갱신 후 board에 쓸 게 있는지 확인.


# board출력하는 함수.
def printBoard():
    for i in range(9):
        for j in range(9):
            if (board[i][j]):
                print(board[i][j], end=' ')
            else:
                print("□", end=' ')
        print()
    print()


# 끝났는지 확인하는 함수.
def isEnd():
    for i in board:
        # 0이 하나라도 존재하면 True 반환.
        if 0 in i:
            return True
    # for문이 중간에 return으로 끊기지 않았다면, 모든 타일이 숫자로 차있다.
    return False


# 보드초기화.
board = [[3, 0, 0, 8, 0, 1, 0, 0, 2],
         [2, 0, 1, 0, 3, 0, 6, 0, 4],
         [0, 0, 0, 2, 0, 4, 0, 0, 0],
         [8, 0, 9, 0, 0, 0, 1, 0, 6],
         [0, 6, 0, 0, 0, 0, 0, 5, 0],
         [7, 0, 2, 0, 0, 0, 4, 0, 9],
         [0, 0, 0, 5, 0, 9, 0, 0, 0],
         [9, 0, 4, 0, 8, 0, 7, 0, 5],
         [6, 0, 0, 1, 0, 7, 0, 0, 3]]
# possibles초기화.
possibles = []
for i in range(9):
    possibles.append([])
    for j in range(9):
        if board[i][j]:
            possibles[i].append([board[i][j]])
        else:
            possibles[i].append([_ for _ in range(1, 10)])

# 보드 출력
printBoard()
# 게임이 끝날 떄 까지.
while isEnd():
    # 가로풀기.
    line_horizontal()
    # 출력.
    printBoard()
    # 세로풀기.
    line_vertical()
    # 출력.
    printBoard()
    # 박스 풀기
    line_box()
    # 출력.
    printBoard()
