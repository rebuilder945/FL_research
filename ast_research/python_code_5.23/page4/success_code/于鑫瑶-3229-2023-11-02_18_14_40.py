ls=eval(input())
ls1=[]
for i in ls:
    if ls.count(i)==1:
        ls1.append(i)
        ls1.sort()
print(ls1)


