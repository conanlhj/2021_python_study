# Sol 1
n = int(input())
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(1)
else:
    print(0)

# Sol 2
a = int(input())
print(int((a % 4 == 0 and a % 100 != 0) or a % 400 == 0))
