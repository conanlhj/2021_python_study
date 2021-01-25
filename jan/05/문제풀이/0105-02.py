list = [1, 'a', 'b', ['b', 'A', ['Hello World!', 2], 'B'], 3, ['C']]
print(list[3][2][0])
# list[3] => ['b', 'A', ['Hello World!', 2], 'B']
# list[3]은 list 타입
# list[3][2] => ['Hello World!', 2]
# list[3][2]도 list 타입
# list[3][2][0] => 'Hello World!'
