n,m=input().split()
n,m=int(n),int(m)
ls=[]
if type(n)!=int or type(m)!=int or n<0 or m<0:
    ls=[]
else:
    for i in range(n,m):
        i=str(i)
        for x in range(n,m):
            x=str(x)
            for y in range(n,m):
                y=str(y)
                z=i+x+y
                if int(i)!=0 and i!=x and x!=y and y!=i and len(z)==3 not in ls:
                    ls.append(z)
if ls==[]:
    print('illegal input')
else:
    print(''.join(a for a in ls))
