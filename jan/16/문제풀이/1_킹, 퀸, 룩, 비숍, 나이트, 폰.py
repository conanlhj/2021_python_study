# Sol 1
chess = [1, 1, 2, 2, 2, 8]
have = list(map(int, input().split()))
for i in range(len(chess)):
    print(chess[i]-have[i], end=' ')

# Sol 2
print(*[i-j for i, j in zip([1, 1, 2, 2, 2, 8], list(map(int, input().split())))])
