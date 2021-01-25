# Sol 1
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print()

# Sol 2
n = int(input())
for i in range(n):
    print(' '*(n-i)+'*'*(i+1))
