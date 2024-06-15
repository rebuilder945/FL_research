lis=input().split(' ')
n=eval(lis[0])
m=eval(lis[1])
if type(m)==int and type(n)==int and m>n and m-n>2:
    lis1=[x for x in range(n,m)]
    lis2=[]
    lis3=[]
    for j in lis1:
        lis2.append(j)
        for y in lis1:
            if y!=j:
                lis2.append(y)
                for z in lis1:
                    if z!=y and z!=j:
                        p=int(str(j)+str(y)+str(z))
                        if p>100:
                            lis3.append(p)
        lis2=[]
    lis3.sort()
    for x in lis3:
        print(x,end=' ')
else:
    print('illegal input')

