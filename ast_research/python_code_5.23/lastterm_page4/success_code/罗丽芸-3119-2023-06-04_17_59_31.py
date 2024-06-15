ls=eval(input())
for x in ls:
    a=ls.count(x)
    if a >=2:
        ls.remove(a)
print(ls)

