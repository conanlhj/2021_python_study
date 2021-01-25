w = [list(input()) for i in range(5)]
m = [len(i) for i in w]
for _ in w:
    for i in range(max(m) - len(_)):
        _.append('')
print(''.join([''.join(_) for _ in zip(*w)]))
