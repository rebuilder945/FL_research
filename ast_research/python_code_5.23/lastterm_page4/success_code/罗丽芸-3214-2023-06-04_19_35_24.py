ls=eval(input())
b=[]
for x in ls:
    if x==0:
        b.append(x)
        ls.remove(0)
    else:
        pass
ls.extend(b)
print(ls)

