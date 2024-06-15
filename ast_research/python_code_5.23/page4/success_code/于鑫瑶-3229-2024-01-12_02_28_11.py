ls=eval(input())
ls2=[]
for i in ls:
    if ls.count(i)==1:
        ls2.append(i)
ls2.sort()
if len(ls2)>0:
    b=",".join(str(i) for i in ls2)
    print(i)
else:
    print("False")
