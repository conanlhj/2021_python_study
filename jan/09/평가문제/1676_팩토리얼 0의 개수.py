# Sol 1
# 팩토리얼 구하기.
f = 1
for i in range(2, int(input())+1):
    f *= i
sf = str(f)
# 뒤에서부터 '0'의 개수 세기.
for i in range(len(sf)):
    if sf[len(sf)-i-1] != '0':
        print(i)
        break

# Sol 2
# 뒤에서 0의 개수가 늘기 위해서는,
# 팩토리얼에서 10의 개수를 찾으면 된다.
# 따라서 5, 25, 125와 같은 5의 제곱수의 개수를 세면 된다.
n = int(input())
print(n//5+n//25+n//125)
