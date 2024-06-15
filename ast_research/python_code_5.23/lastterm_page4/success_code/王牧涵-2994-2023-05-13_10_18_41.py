sum=input().split(",")
n,m=input().split(",")
n=int(n)
m=int(m)
list1=[]
   
for x in sum:
    list1.append(x)
    list2=list1.copy()
    if n<=len(list1): 
        w=sum[n]
        print(w)
        for i in range(m):
           list2.append(w)   
list2=[int(b) for b in list2]     
    
print(list2)
