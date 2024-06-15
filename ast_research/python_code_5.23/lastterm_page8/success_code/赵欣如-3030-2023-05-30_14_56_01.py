ls1=input().split(",")
ls2=list(eval(input()))
ls5=ls2.copy()
ls2.sort()
ls4=[]
for i in ls2:
    a=ls5.index(i)
    ls3=[]
    ls3.append(ls1[a])
    ls3.append(ls5[a])
    ls4.append(ls3)
print(ls4)

    

