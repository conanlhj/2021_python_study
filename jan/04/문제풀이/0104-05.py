# Sol 1
for _ in range(int(input())):
    tmp = ""
    a, b = input().split()
    for i in b:
        tmp += i*int(a)
    print(tmp)

# Sol 2
for _ in range(int(input())):
    a, b = input().split()
    for i in b:
        print(i*int(a), end='')
    print()

# Sol 3
for _ in range(int(input())):
    a, b = input().split()
    print(''.join([i*int(a) for i in b]))
