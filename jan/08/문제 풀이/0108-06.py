n, k = map(int, input().split())

for i in range(n):
    if n == 1 or not i % (n-1):
        print('*'*n)
    else:
        for j in range(n):
            if (i+j+1) % k == 0 or not j % (n-1):
                print('*', end='')
            else:
                print(' ', end='')
        print()
