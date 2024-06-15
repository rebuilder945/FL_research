a=eval(input())
b=[a.count(x) for x in a]
if (b.count(1)==0) :
        print("False")
if (b.count(1)!=0):
    result=[]
    for i in b:
        if (i!=1):
            continue
        if (i==1):
            n=b.index(i)
            b[n]=0
            result.append(a[n])
    result.sort()
    print(",".join(str(x) for x in result))
    
    

        
