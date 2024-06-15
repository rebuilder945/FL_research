m=eval(input())
n=[]
for i in m:
    l=[]
    l=list(range(2,i))
    for x in l:
        if i%x==0:
            n.append(i)
k=[]
for x in m:
    if x not in n and x!=0 and x!=1:
        k.append(x)
print(k)
 

