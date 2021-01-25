n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]

result = 0
for i in money[::-1]:
    result += k//i
    k -= (k//i)*i

print(result)
