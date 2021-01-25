n, win = input().split()
info = []
aTotal = bTotal = 0
for i in range(int(n)):
    tmp = input().split()
    if tmp[1] == 'A':
        aTotal += int(tmp[2])
    else:
        bTotal += int(tmp[2])
    info.append(tmp)

aOdds, bOdds = (aTotal+bTotal)/aTotal, (aTotal+bTotal)/bTotal
winOdds = aOdds if win == 'A' else bOdds

print("%.2f %.2f" % (aOdds, bOdds))
for i in info:
    if i[1] == win:
        print(i[0], round(int(i[2])*winOdds))
    else:
        print(i[0], 0)
