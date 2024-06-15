ls=eval(input())
for x in ls:
    if ls.count(x)>1:
        for i in range(ls.count(x)-1):
            ls.remove(x)
    else:
        break
print(ls)
