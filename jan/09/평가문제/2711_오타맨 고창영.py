for i in range(int(input())):
    a, b = input().split()
    print(b[:int(a)-1]+b[int(a):])
