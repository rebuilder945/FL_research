n=eval(input())
ls=[x for x in range(1,1+n)]
for i in range(len(ls)):
    ls[i],ls[i-1]=ls[i-1],ls[i]
ls[-1],ls[-2]=ls[-2],ls[-1]
print(ls)
