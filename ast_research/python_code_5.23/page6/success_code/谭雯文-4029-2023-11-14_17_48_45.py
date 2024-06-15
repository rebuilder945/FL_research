n,m=map(int,input().split())
if 0<=n<m<=10 and m-n>=3:
    for i in range(n,m):
        for a in range(n,m):
            for c in range(n,m):
                shu=i*100+a*10+c
                if shu>99 and i!=a and i!=c and c!=a :
                    print(shu)
else:    
    print("illegal input")


            


# else:
#     print("illegal input")            
                
                
                
