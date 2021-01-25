# Sol 1
n, stack, r = int(input()), [], []
cnt, i, result = 0, 1, []
t_result = [int(input()) for _ in range(n)]

while r != t_result:
    if len(stack) == 0:
        stack.append(i)
        i += 1
        result.append('+')
    if t_result[cnt] == stack[-1]:
        r.append(stack.pop())
        cnt += 1
        result.append('-')
    else:
        stack.append(i)
        i += 1
        result.append('+')
    if i > n+1:
        print('No')
        break
if i <= n+1:
    print(*result, sep='\n')

# Sol 2
n = int(input())
t = [int(input()) for _ in range(n)][::-1]
s, i, result = [], 1, []
while len(t):
    if i > n+1:
        print('No')
        break
    try:
        if t[-1] == s[-1]:
            t.pop()
            s.pop()
            result.append('-')
        else:
            s.append(i)
            i += 1
            result.append('+')
    except IndexError:
        s.append(i)
        i += 1
        result.append('+')
if i <= n+1:
    print(*result, sep='\n')
