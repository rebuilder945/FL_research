a=input().split()
b={}
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1
nums=list(b.values())
a=max(nums)
maxx=[]
lst=sorted(list(b.items()))
for v,t in lst:
    if t==a:
        print(v,t)





    









            
