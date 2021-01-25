arr = [-1 for i in range(26)]
line = input()
for i in range(len(line)):
    if arr[ord(line[i]) - ord('a')] == -1:
        arr[ord(line[i]) - ord('a')] = i
for i in arr:
    print(i, end=' ')
