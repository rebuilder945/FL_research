lst = eval(input())
new = []
cnt = 0
for x in lst:
    if x != 0:
        new.append(x)
    else:
        cnt += 1
new += [0] * cnt
print(new)



