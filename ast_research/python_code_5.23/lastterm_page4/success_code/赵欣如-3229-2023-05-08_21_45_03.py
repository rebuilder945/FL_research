a=eval(input())
b=[a.count(x) for x in a]
if 1 not in b :
        print("False")
if 1 in b:
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
    
    

        
