arr = []
for i in range(10):
    n = int(input()) % 42
    if n not in arr:
        arr.append(n)
print(len(arr))
