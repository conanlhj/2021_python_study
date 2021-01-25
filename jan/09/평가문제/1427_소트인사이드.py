# Sol 1
a = list(map(int, list(input())))
a.sort(reverse=True)
for i in a:
    print(i, end='')

# Sol 2
print(*sorted(input(), reverse=True), sep='')
