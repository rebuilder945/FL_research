ls = eval(input())
ls.reverse()
x = []
for m in ls:
    if m not in x:
        x.append(m)
x.reverse()
print(x)
