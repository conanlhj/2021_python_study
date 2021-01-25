# Sol 1
sumlist = input().split('-')
sublist = []
for i in sumlist:
    sum = 0
    for j in i.split('+'):
        sum += int(j)
    sublist.append(sum)
result = sublist[0]
for i in sublist[1:]:
    result -= i
print(result)

# Sol 2
sumlist = input().split('-')
sublist = []
for i in sumlist:
    sublist.append(eval(i))
result = sublist[0]
for i in sublist[1:]:
    result -= i
print(result)
