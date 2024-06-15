n,m=map(int,input().split(" "))
lst=[]
if m-n<3 or m>10 or n<0:
    print("illegal input")
else:
    for i in range(m-n):
        lst.append(n+i)
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i!=j and j!=k and i!=k:
                print(str(lst[i])+str(lst[j])+str(lst[k]),end=" ")
        
    
    
    

