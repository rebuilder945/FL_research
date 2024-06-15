n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
for x in l:
    if x<n:
        x+=1
    elif x==n:
        x=1    
print(l)
