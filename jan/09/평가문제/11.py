n, b = map(int, input().split())
if b == 2:
    print(bin(n)[2:])
elif b == 8:
    print(oct(n)[2:])
else:
    print(hex(n)[2:])
