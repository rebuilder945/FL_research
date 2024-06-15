ls=eval(input())
ls.reverse()
ls1=[]
num=0
for x in ls:
    if ls.count(x)==1:
        num+=1
        if x not in ls1:
            ls1.append(x)
ls1.reverse()
ls1.sort()
if num==0:
    print("False")
else:
    print(",".join(str(i)for i in ls1))
