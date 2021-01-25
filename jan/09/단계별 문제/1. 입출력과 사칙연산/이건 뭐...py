print("강한친구 대한육군")
print("강한친구 대한육군")

# 출력할 때 \이 기호를 그냥 쓸 수 없음에 유의
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

# ",\와 같은 특수기호 주의
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

print(sum(map(int, input().split())))

a, b = map(int, input().split())
print(a - b)

a, b = map(int, input().split())
print(a * b)

a, b = map(int, input().split())
print(a / b)

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

A, B, C = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
