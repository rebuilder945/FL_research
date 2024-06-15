a=input().split(" ")
n=int(a[0])
m=int(a[1])
b=[]
if n>=m or m<=2:
    print("illegal input")
else:
    for i in range(n,m):
        n1=i
        for i in range(n,m):
            n2=i
            if i!=n1:
              
                N1=n1+n2*10
            
                for i in range(n,m):
                   n3=i
                   if i!=n1 and i!=n2:
                  
                     N2=n3*100+N1
                     b.append(N2)
                     b.reverse()
    print(" ".join(str(i) for i in b ))



