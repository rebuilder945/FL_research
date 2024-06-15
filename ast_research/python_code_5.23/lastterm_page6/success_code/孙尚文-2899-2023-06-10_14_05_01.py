a=input().split()
a=list(map(int,a))
b,c=a[0],a[1]
if 0<=b<c<11 and c-b==3:
    for i in range(int(b),int(c)):
        for j in range(int(b),int(c)):
            for k in range(int(b),int(c)):
                if i!=j and j!=k and k!=i:
                    m=100*i+10*j+k

                    if m>99:
                        print(m,end=" ")
else:
    print("illegal input")
    

