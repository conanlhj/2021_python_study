cats = sorted(map(int, input().split()))
cnt = 0
flag = False
while not flag:
    cnt += cats[0]
    flag = True
    for i in cats[1:]:
        if cnt % i:
            flag = False
            break
print(cnt)
