ls = eval(input())
new = []
for x in ls:
    if x not in new:
        new.append(x)
print(new)
