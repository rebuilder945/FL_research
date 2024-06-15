def work(a) :
    lis=[]
    lis1=[]
    for x in range(0,a+1):
        lis1.append(x)
        if x==0:
            lis.append(1)
        elif x!=0:
            w=1
            for k in range(1,x+1):
                w*=k
            lis.append(w)
    kk=dict(zip(lis1,lis))           
    return kk
	

a = int(input())
ans = work(a)
print(ans)

