ls=eval(input())
a=0
ls1=[]
for x in ls:
    if ls.count(x)==1:
        ls1.append(x)
    else:
        a+=1
if a==len(ls):
    print("False")
else:
    ls1.sort()
    print(*ls1,sep=",")
