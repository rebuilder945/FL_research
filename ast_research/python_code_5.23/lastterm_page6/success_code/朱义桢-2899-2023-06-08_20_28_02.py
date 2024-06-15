a=input().split()
n=eval(a[0])
m=eval(a[1])
if m-n<3 or m<3 or n<0:
    print("illegal input")
else:
    b=list(x for x in range(n,m))
    d=[]
    for x in b:
        for y in b:
            for z in b:
                if x!=y and y!=z and x!=z and x!=0:
                    d.append(100*x+10*y+z)
    d.sort(reverse=False)
    for x in d:
        print(x,end=" ")
