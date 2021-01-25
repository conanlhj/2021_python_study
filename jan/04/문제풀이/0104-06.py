# Sol 1
arr = []
for i in range(10):
    n = int(input()) % 42
    if n not in arr:
        arr.append(n)
print(len(arr))

# Sol 2
arr = []
for i in range(10):
    arr.append(int(input()) % 42)
print(len(set(arr)))

# Sol 3
print(len({int(input()) % 42 for i in range(10)}))
