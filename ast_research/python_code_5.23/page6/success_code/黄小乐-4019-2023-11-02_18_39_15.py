n=input().split()
ls=list(map(int,n))
for x in ls:
    x=(x+5)%10
l=len(ls)
if l%2==0:
    for i,j in [(0,l/2),(l/2,l)]:
        ls[i],ls[j]=ls[j],ls[i]
else:
    for i,j in [(0,int(l/2)),(int(l/2)+1,l)]:
         ls[i],ls[j]=ls[j],ls[i]
print(ls)






