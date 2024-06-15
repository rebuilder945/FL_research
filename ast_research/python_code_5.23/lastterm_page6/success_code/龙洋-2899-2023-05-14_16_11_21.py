lis=input().split(' ')
n=eval(lis[0])
m=eval(lis[1])
if type(m)==int and type(n)==int and m>n:
    lis1=[x for x in range(n,m)]
    lis2=[]
    lis3=[]
    for j in lis1:
        lis2.append(j)
        for y in lis1:
            if y not in lis2:
                lis2.append(y)
                for z in lis1:
                    if z not in lis2:
                        p=int(str(j)+str(y)+str(z))
                        if p>100:
                            lis3.append(p)
        lis2=[]
    lis3.sort()
    print(lis3)
else:
    print('illegal input')

