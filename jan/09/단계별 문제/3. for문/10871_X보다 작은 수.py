n, x = map(int, input().split())
a = map(int, input().split())
for j in a:
    if j < x:
        print(j, end=' ')
