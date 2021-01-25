r = []
for i in range(int(input())):
    lst = list(map(int, input().split()))
    avg = sum(lst[1:])/lst[0]
    cnt = 0
    for i in lst[1:]:
        if i > avg:
            cnt += 1
    r.append(100*cnt/(len(lst)-1))
for i in r:
    print("%.3f" % i+'%')
