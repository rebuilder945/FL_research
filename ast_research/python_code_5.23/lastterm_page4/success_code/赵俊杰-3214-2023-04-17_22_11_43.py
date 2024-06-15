ls=eval(input())
for x in ls:
    if int(x)==0:
        ls.remove(0)
        ls.append(0)
    else:
        pass
print(ls)
