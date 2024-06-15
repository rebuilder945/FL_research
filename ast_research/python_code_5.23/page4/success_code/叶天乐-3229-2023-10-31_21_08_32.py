ls1 = eval(input())
ls2 = []
for i in ls1:
    if ls1.count(i)==1:
        ls2.append(i)
if len(ls2)==0:
    print("False")
else:
    ls2.sort()
    print(ls2)
 

       

