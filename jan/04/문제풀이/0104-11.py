def f(n):
    print(n)
    if n % 2 and n > 1:
        f(3*n+1)
    elif not n % 2:
        f(n//2)


f(int(input()))
