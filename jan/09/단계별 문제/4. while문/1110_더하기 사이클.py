# Sol 1
i = int(input())
ten = i // 10
one = i % 10
cnt = 0
while True:
    cnt += 1
    tmp = one
    one = (ten+one) % 10
    ten = tmp
    if ten == i//10 and one == i % 10:
        break
print(cnt)


# Sol 2
n = int(input())
f = n
c = 0
while (c == 0)+n-f:
    c += 1
    n = (n % 10) * 10 + (n*11//10) % 10
print(c)
