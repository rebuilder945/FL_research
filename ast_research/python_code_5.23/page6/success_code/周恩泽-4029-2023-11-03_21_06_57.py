n,m=map(int,input().split(" "))
if n>m-3 or type(n)!=int or type(n)!=int:
    print("illegal input")
else:
    a=[]
    for x in range(n,m):
        a.append(str(x))
    
    m=[]
    for i in a:
        for x in a:
            for y in a:
                c=i+x+y
                if i!=x and i!=y and x!=y:
                    m.append(c)
    
    l=[]
    for x in m:
        if int(x[0])==0:
            print(x)
            l.append(x)
p=[x for x in m if x not in l]
print(p)

    


