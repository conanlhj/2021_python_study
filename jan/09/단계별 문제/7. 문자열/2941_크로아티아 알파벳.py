cr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
line = input()
for i in cr:
    line = line.replace(i, '*')
print(len(line))
