# Sol 1
x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)

# Sol 2
x = int(input())
y = int(input())
print([[3, 2], [4, 1]][x > 0][y > 0])
