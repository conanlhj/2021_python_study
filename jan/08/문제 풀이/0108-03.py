# Sol 1
a, r, n = map(int, input().split())
print(a*r**(n-1))

# Sol 2
a, r, n = map(int, input().split())
for i in range(n-1):
    a *= r
print(a)
