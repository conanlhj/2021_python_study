def star(r, c, N):
    if N == 1:
        ans[r][c] = '*'
        return
    for i in range(r, r+N, N//3):
        for j in range(c, c+N, N//3):
            if not (i == r + N//3 and j == c + N//3):
                star(i, j, N//3)


N = int(input())
ans = [[' ' for i in range(N)] for i in range(N)]
star(0, 0, N)
for _ in ans:
    print(''.join(_))
