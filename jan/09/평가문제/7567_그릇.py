# Sol 1
a = '.'
result = 0
for i in input():
    if i != a:
        a = i
        result += 10
    else:
        result += 5
print(result)

# Sol 2
b = input()
print((len(b)+b.count('()')+b.count(')(')+1)*5)
# 그릇이 겹쳐있는 모양을 세면 됨.
# 5*(문자열 길이+'()' 개수+')(' 개수 +1(처음))
