# Sol 1
t = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        del t[-1]
    else:
        t.append(n)
print(sum(t))

# Sol 2
t = []
for i in range(int(input())):
    n = int(input())
    if not n:
        t.pop()
    else:
        t.append(n)
print(sum(t))
