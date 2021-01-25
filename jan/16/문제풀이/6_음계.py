# Sol 1
i = list(map(int, input().split()))
asc = sorted(i)
if asc == i:
    print('ascending')
elif asc[::-1] == i:
    print('descending')
else:
    print('mixed')

# Sol 2
d = {'12345678': 'ascending', '87654321': 'descending'}
try:
    print(d[''.join(input().split())])
except:
    print('mixed')
