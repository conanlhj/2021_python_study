cord = []
for i in range(int(input())):
    cord.append(list(map(int, input().split())))
cord.sort()
for x, y in cord:
    print(x, y)
