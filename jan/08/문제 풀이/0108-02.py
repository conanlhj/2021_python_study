# Sol 1
sumN = 0
for i in range(int(input())+1):
    if not i % 2:
        sumN += i
print(sumN)

# Sol 2
print(sum(range(0, int(input())+1, 2)))
