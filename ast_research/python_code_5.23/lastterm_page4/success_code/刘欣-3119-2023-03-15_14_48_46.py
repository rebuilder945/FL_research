ls=eval(input())
newls=[]
for i in ls:
    if ls.conut(i)>1:
        while i in ls:
            ls.remove(i)
        newls.append(i)
    else:
        ls.conut(i)==1
        newls.append(i)
print(newls)
