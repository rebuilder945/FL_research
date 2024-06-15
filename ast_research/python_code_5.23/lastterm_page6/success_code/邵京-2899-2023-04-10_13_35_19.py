n,m=input().split()
a=int(n)
b=int(m)
if a<b and b-a==3 and a>0:
    for i in range(a,b):
        for j in range(a,b):
            for x in range(a,b):
                if i!=j and j!=x and i!=x:
                    print(i,j,x)
else:
    print('illegal input')
