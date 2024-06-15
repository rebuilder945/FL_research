ls = eval(input())
new = []
ls.reverse()
for x in ls:
    if x not in new:
        new.append(x)
print(new)
