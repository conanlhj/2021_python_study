def d(n, sum):
    if sum == 0:
        sum += n
    sum += n % 10
    if n < 10:
        return sum
    return d(n//10, sum)


list = [i for i in range(1, 10001)]
for i in range(1, 10001):
    tmp = d(i, 0)
    if tmp in list:
        list.remove(tmp)
for i in list:
    print(i)
