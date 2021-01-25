# Sol 1
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

# Sol 2
for i in range(int(input())):
    print('*'*(i+1))
