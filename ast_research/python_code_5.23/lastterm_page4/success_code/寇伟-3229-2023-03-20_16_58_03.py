ls=[]
ls1=eval(input())
m=0
for i in ls1:
    if ls1.count(i)==1:
        ls.append(i)
    else:
        m+=1
        if m==len(ls1):
            print(False)

