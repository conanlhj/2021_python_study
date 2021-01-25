# Sol 1
n = int(input())
for _ in range(n):
    for i in range(_):
        print(' ', end='')
    for i in range(n-_):
        print('*', end='')
    print()

# Sol 2
n = int(input())
for i in range(n):
    print(' '*i+'*'*(n-i))
# 문자열*정수는 문자열을 정수만큼 반복,
# 문자열+문자열은 문자열 두개를 더함.
# 이 두가지를 이용함.
