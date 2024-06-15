n,m = list(map(int,input().split()))
if m<=n+2 or m<0 or n<0 or n>=8:
    print("illegal input")
else:
    lst=[]
    lst1=list(range(n,m))
    for x in lst1:
        for y in lst1:
            for z in lst1:
                if x!=y and y!=z and x!=z :
                    s1 = str(x)+str(y)+str(z)
                    lst.append(s1)
    for i in lst:
        i = int(i)
        print(i,end=" ")

                    
                    




    
