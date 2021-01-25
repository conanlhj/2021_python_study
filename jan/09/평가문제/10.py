n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        print("%02d " % (j+1+i*m), end='')
    print()
