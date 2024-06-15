ls=eval(input())
ls1=[]
for x in ls:
    if ls.count(x)!=1:
        ls.remove(x)
        ls.insert(0,' ')
for y in ls:
    if y!=' ':
        ls1.append(y)
print(ls1)











