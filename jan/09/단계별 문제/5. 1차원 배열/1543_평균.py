# Sol 1
input()
s = list(map(int, input().split()))
scores = []
for i in s:
    scores.append(i/max(s)*100)
print(sum(scores)/len(scores))

# Sol 2
input()
s = list(map(int, input().split()))
print(sum(100*i/max(s) for i in s)/len(s))
