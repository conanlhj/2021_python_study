words = input().lower()
s = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
time = 0
for i in words:
    for j in s:
        if i in j:
            time += s.index(j) + 3
print(time)
