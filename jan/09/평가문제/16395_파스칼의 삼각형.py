def f(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


n, k = map(int, input().split())
print(f(n-1)//(f(k-1)*f(n-k)))
