# Sol 1
n = int(input())
for i in range(n):
    print(n-i)

# Sol 2
print(*range(int(input()), 0, -1))
