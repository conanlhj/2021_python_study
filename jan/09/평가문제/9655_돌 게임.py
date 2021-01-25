# Sol 1
if int(input()) % 2:
    print('SK')
else:
    print('CY')

# Sol 2
print('SK' if int(input()) % 2 else 'CY')

# 이 문제를 정말 쉽게 생각해보자.
# 1개또는 3개만 가져갈 수 있다.
# 홀수개만 가져갈 수 있는 것.
# 그래서 시작하는 수가 홀수개라면,
# 상근이가 이기고, 짝수개면 창영이가 이긴다.
