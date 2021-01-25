# Sol 1
a = 1
for i in range(3):
    a *= int(input())
b = [0 for i in range(10)]
for i in str(a):
    b[int(i)] += 1
for i in b:
    print(i)

# Sol 2
a = eval('*'.join([input() for i in range(3)]))
for i in range(10):
    print(str(a).count(str(i)))
