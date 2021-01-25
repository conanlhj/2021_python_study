str = list(input())
for i in range(len(str)):
    str.insert(0, str.pop())
    print(''.join(str))
