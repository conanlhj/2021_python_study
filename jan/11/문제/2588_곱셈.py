a, b = int(input()), input()
print(*[a*int(_) for _ in b][::-1], a*int(b))
