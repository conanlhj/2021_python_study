# Sol 1
for _ in range(int(input())):
    tmp = ""
    a, b = input().split()
    for i in b:
        tmp += i*int(a)
    print(tmp)


# Sol 2
for t in range(int(input())):
    a, b = input().split()
    print(''.join([i*int(a) for i in b]))
