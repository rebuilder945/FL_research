ls = eval(input())
for x in ls:
    if ls.count(x)>1:
        for y in range(ls.count(x)-1):
            ls.remove(x)
print(ls)
