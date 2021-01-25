# Sol 1
h, m = map(int, input().split())
if m - 45 >= 0:
    print(h, m-45)
elif h == 0:
    print(23, 15+m)
else:
    print(h-1, 15+m)

# Sol 2
h, m = map(int, input().split())
print((h-(m < 45)) % 24, (m-45) % 60)
