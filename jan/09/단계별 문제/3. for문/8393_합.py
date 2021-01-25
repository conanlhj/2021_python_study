# Sol 1
s = 0
for i in range(int(input())+1):
    s += i
print(s)

# Sol 2
n = int(input())
print(n*(n+1)//2)

# Sol 3
print(sum([i for i in range(1, int(input())+1)]))
