# Sol 1
n = int(input())
for _ in range(n):
    for i in range(n):
        if _ % 2:
            print(' ', end='*')
        else:
            print('*', end=' ')
    print()
# 가장 정석?

# Sol 2
n = int(input())
for _ in range(n):
    print(" "*(_ % 2), "* "*n, sep="")
# 현재 줄이 짝수 홀수인지에 따라서,
# 맨 처음 한칸 띄우고 시작할지 바로 시작할지 정함.
# 그 다음 "* "을 n번만큼만 출력하면 됨.
