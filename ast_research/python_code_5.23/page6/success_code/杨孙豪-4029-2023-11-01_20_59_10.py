n,m=input().split()
n,m=int(n),int(m)
if n>=m or m-n<=2 or n*m<0 or m>9:
    print('illegal input')
else:
    lst=[x for x in range(n,m)]
    bst=[]
    for x in lst:
        for y in lst:
            for z in lst:
                 if x!=y and y!=z and x!=z and x!=0:
                      bst.append(x*100+y*10+z)
    cst=list(map(str,bst))
    print(' '.join(cst))



