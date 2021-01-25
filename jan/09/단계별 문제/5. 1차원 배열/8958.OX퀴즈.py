# Sol 1
for _ in range(int(input())):
    n = 0
    sum = 0
    for i in input():
        if i == 'X':
            n = 0
            continue
        n += 1
        sum += n
    print(sum)

# Sol 2
for _ in range(int(input())):
    a = input().split('X')
    sum = 0
    for i in a:
        if i:
            sum += len(i)*(len(i)+1)//2
    print(sum)
