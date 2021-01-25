# 단어가 있는 인덱스 반환, 없으면 -1반환
def isWordInLine(line, word):
    return line.find(word.upper())


# 가로줄 찾기
def solveHorizontal(word):
    # 가로줄 string 타입으로 join후 list에 저장
    lines = [''.join(str) for str in board]
    # 각 줄에 대해 반복
    for i in range(MAX_Y):
        # r에 해당 word가 있는 index 또는 -1 저장
        r = isWordInLine(lines[i], word)
        # -1이면 다음줄로 넘어가기.
        if r == -1:
            continue
        # 찾는 단어가 해당 줄에 있으면 resultBoard에 업데이트
        for j in range(len(word)):
            resultBoard[i][r+j] = '★'
        words[word] = 'O'
        return True
    return False


# 세로줄 찾기
def solveVertical(word):
    # 세로줄 string 타입으로 join후 list에 저장
    lines = [''.join(str) for str in zip(*board)]
    # 각 세로줄에 대해 반복
    for i in range(MAX_X):
        # r에 해당 word가 있는 index 또는 -1 저장
        r = isWordInLine(lines[i], word)
        # -1이면 다음줄로 넘어가기.
        if r == -1:
            continue
        # 찾는 단어가 해당 줄에 있으면 resultBoard에 업데이트
        for j in range(len(word)):
            resultBoard[r+j][i] = '●'
        words[word] = 'O'
        return True
    return False


# 좌하향 대각선 찾기(↙)
def solveDiagonal_p(word):
    # 모든 대각선에 대해서
    for d in range(MAX_X+MAX_Y-1):
        # line 설정.
        line = ''
        for i in range(MAX_Y):
            for j in range(MAX_X):
                if i+j == d:
                    line += board[i][j]
        # r에 해당 word가 있는 index 또는 -1
        r = isWordInLine(line, word)
        # -1 인 경우 다음줄로 넘어가기
        if r == -1:
            continue
        # 찾는 단어가 해당 줄에 있으면 resultBoard 업데이트
        if d >= MAX_X:
            x, y = MAX_X-1-r, d+r-MAX_X+1
        else:
            x, y = d-r, r
        for i in range(len(word)):
            resultBoard[y+i][x-i] = '◀'
        words[word] = 'O'
        return True
    return False


# 우하향 대각선 찾기(↘)
def solveDiagonal_m(word):
    # 모든 대각선에 대해서
    for d in range(MAX_X+MAX_Y-1):
        # line 설정.
        line = ''
        for i in range(MAX_Y):
            for j in range(MAX_X):
                if i-j+MAX_X-1 == d:
                    line += board[i][j]
        # r에 해당 word가 있는 index 또는 -1
        r = isWordInLine(line, word)
        # -1 인 경우 다음줄로 넘어가기
        if r == -1:
            continue
        # 찾는 단어가 해당 줄에 있으면 resultBoard 업데이트
        if d >= MAX_X:
            x, y = r, d-MAX_X+1
        else:
            x, y = MAX_X-1-d+r, r
        for i in range(len(word)):
            resultBoard[y+i][x+i] = '▶'
        words[word] = 'O'
        return True
    return False


# board.txt 읽어와서 board 리스트 만들기.
f = open('board.txt', 'r')
board = f.read().split('\n')
for i in range(len(board)):
    board[i] = board[i].split()
f.close()
MAX_X = len(board[0])
MAX_Y = len(board)

# 출력할 board
resultBoard = [[chr+' ' for chr in str] for str in board]

# words.txt파일 읽어와서 words 리스트 만들기.
f = open('words.txt', 'r')
words = {}
for word in f.read().split():
    words[word] = 'X'
    words[word[::-1]] = 'X'
f.close()

for word in words:
    if (solveHorizontal(word) or
        solveVertical(word) or
        solveDiagonal_p(word) or
       solveDiagonal_m(word)):
        continue

print(*[' '.join(line) for line in resultBoard], sep='\n')
for k, v in words.items():
    print(k, v)
