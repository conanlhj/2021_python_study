# 숫자 업데이트 하는 함수.
def getnum(c_num):
    c_num += 1
    if c_num == n+1:
        return 1
    return c_num


# 리스트 돌리는 함수.
def rotatebox(box):
    rotate = [[0]*l for i in range(l)]
    for i in range(l):
        for j in range(l):
            rotate[j][l-i-1] = box[i][j]
    return rotate


# 입력 & 초기화.
l, n, m = [int(input()) for _ in range(3)]
c_num = 1
box = []
# 모양 잡아두기.
for i in range(l):
    tmp = []
    for j in range(i+1):
        tmp.append(str(c_num))
        c_num = getnum(c_num)
    for j in range(l-i-1):
        tmp.append(' ')
    box.append(tmp)

# 돌리면서 출력하기.
for i in range(m):
    for j in range(l):
        print(''.join(box[j]))
    print()
    box = rotatebox(box)
