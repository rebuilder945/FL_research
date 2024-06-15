ls=eval(input())
ls1=[]
for i in ls:
    if ls1.count(i)==1:
        ls1.append(i)
if len(ls1) > 0:
    print(ls1.sort())
else:
    print("False")
