# Sol 1
for k in range(int(input())):
    p, m = map(int, input().split())
    c = [False for _ in range(m)]
    fail = 0
    for i in range(p):
        n = int(input())
        if c[n-1]:
            fail += 1
        else:
            c[n-1] = True
    print(fail)

# Sol 2
for k in range(int(input())):
    p, m = map(int, input().split())
    s = set()
    for i in range(p):
        s.add(input())
    print(p-len(s))
