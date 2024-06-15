ls=eval(input())
ls1=[]
if min(ls.count(s) for s in range(0,len(ls)))<2:
    for i in range(0,len(ls)):
        if ls.count(ls[i])==1:
            ls1.append(ls[i])
            ls1.sort()
            print(ls1(z) for z in range(0,len(ls1)))
else:
    print("False")



