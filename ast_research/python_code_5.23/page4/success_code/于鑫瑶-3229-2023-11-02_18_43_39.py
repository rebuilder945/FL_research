ls=eval(input())
ls1=[]
for i in ls:
    if ls.count(i)==1:
        ls1.append(i)
        ls1.sort()
        a=str(ls1).strip("[]")
        a=eval(a)
print(a)



