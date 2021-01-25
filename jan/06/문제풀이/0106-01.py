# Sol 1
for _ in range(int(input())):
    for i in range(_+1):
        print('*', end='') # 파이썬에서 print문은 자동으로 줄바꿈을 하므로, end=''을 이용해서 끝을 지정해줘야함.
    print()
# 가장 많이 하는 방법이고, c와 java에서 사용한 방법.

# Sol 2
for i in range(int(input())):
    print('*'*(i+1))
# 약간 까리
