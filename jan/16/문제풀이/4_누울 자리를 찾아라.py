r = [input() for i in range(int(input()))]
# h = ('X'.join(r)+'X').count('..X')
# v = ('X'.join([''.join(_) for _ in zip(*r)])+'X').count('..X')
# print(h, v)
print(('X'.join(r)+'X').count('..X'), ('X'.join([''.join(_) for _ in zip(*r)])+'X').count('..X'))
