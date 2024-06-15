a=input().split(" ")
n=int(a[0])
m=int(a[1])
if n>=m-2 or n<0 or m>9:
    print('illegal input')
else:
    a=[x for x in range(n,m)]
    b=[]
    for x in a:
        for y in a:
            for z in a:
                if x!=y and x!=z and y!=z and x!=0:
                    b.append(100*x+10*y+z)
    for x in b:
        print(x,end=" ")
