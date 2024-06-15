ls=eval(input())
ls2=[]
for x in ls:
    if ls.count(x)==1:
        ls2.append(x)
    else:
        pass
if len(ls2)==0:
    print("False")
else:
    for i in ls2:
        print(i)
