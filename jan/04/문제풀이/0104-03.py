# Sol 1
n = int(input())
for i in range(n):
    print(n-i)

# Sol 2
for i in range(int(input()), 0, -1):
    print(i)

# Sol 3
print(*range(int(input()), 0, -1))
