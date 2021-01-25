x, y = 1, 1
map = [input().split() for _ in range(10)]
while True:
    map[y][x] = '9'
    # 먹이.
    if map[y][x+1] == '2':
        map[y][x+1] = '9'
        break
    elif map[y+1][x] == '2':
        map[y+1][x] = '9'
    # 오른쪽이동 가능하면.
    if map[y][x+1] == '0':
        x += 1
    # 아래이동 가능하면.
    elif map[y+1][x] == '0':
        y += 1
    else:
        break
for i in map:
    print(' '.join(i))
