for t in range(int(input())):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    isTarget = [False for i in range(n)]
    isTarget[m] = True
    cnt = 0

    while True:
        if queue[0] == max(queue):
            cnt += 1
            if isTarget[0]:
                print(cnt)
                break
            queue.pop(0)
            isTarget.pop(0)
        else:
            queue.append(queue.pop(0))
            isTarget.append(isTarget.pop(0))
