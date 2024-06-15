n,m=list(map(int,input().split()))
ls=[]
if (m-n)<3 or n<0 or m>9:
    print('illegal input')
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                a=str(x)+str(y)+str(z)
                ls.append(a)
    for x in ls[::-1]:
        if x[0]=='0' or x[0]==x[1] or x[0]==x[2] or x[1]==x[2]:
            ls.remove(x)
    for x in ls:
        print(x,end=' ')

