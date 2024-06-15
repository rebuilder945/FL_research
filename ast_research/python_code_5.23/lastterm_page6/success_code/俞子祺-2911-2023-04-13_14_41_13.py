ls=list(input())
for i in range(len(ls)):
    ls[i]=eval((ls[i]+5)%10)
ls[0],ls[1],ls[2]=ls[-3],ls[-2],ls[-1]
for i in ls:
    print(i,end=" ")
