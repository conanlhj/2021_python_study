a = list(map(int, input().split()))
b = list(map(int, input().split()))
cross_product = [a[1]*b[2] - a[2]*b[1],
                 a[2]*b[0] - a[0]*b[2],
                 a[0]*b[1] - a[1]*b[0]]
dot_product = sum([i*j for (i, j) in zip(a, b)])
print(cross_product)
print(dot_product)

# 벡터와 관련하여 자세한 내용은 Chapter9에서 배웁니다.
# 위 코드를 더 간단화시키는 방법도 같이 나옵니다.
