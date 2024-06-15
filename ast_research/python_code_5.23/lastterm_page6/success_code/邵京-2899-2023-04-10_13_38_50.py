n,m=input().split()
a=int(n)
b=int(m)
if a<b and a>=0:
    for i in range(a,b):
        for j in range(a,b):
            for x in range(a,b):
                if i!=j and j!=x and i!=x:
                    print(i*100+j*10+x,end='')
else:
    print('illegal input')
