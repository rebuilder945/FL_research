ls=eval(input())
ls2=[]
for i in ls:
    if ls.count(i)==1:
        ls2.append(i)
ls2.sort()
if len(ls2)>0:
    for x in range(len(ls2)):
        print(ls2[x],end=",")
else:
    print("False")
