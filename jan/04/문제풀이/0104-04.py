# Sol 1
list = input().split()
a = int(list[0])
b = int(list[1])
if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")

# Sol 2
a, b = map(int, input().split())
print(">" if a > b else ("<" if a < b else "=="))
