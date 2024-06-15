n,m=map(int,input().split())
for i in range(n,m):
    for a in range(n,m):
        for c in range(n,m):
            shu=str(i)+str(a)+str(c)
            shu1=eval(shu)
            if m-n!=3 and m>10 :
                
                
                print("illegal input")
            elif i!=a and i!=c and c!=a and i!=0 and c!=0:
                shu=eval(input(str(i)+str(a)+str(c)))

            
                print(shu1,end=" ")
