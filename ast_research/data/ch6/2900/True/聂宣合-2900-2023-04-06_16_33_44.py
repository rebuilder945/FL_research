dex=eval(input())
sums=[]
summary=[]

if type(dex) == int and float(dex)>0:                               
    for i in range(2,dex+1):
        for x in range(2,i):
            if i%x== 0:
                break
        else:
            sums.append(i)
    sums=list(set(sums))


    for y in sums:
        x=list(str(y))
        if x == x[::-1]:
            summary.append(y)
    summary.sort()                      #Final dex
    print(" ".join(str(z)for z in summary))
else:
    print("illegal input")

