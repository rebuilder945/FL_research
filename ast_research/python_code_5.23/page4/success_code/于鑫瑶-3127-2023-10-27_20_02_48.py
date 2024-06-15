n=eval(input())
sum=range(1,n+1)
ls1=[]
m=sum[0]
for x in range(len(sum)-1):
    ls1.append(sum[x+1])
ls1.append(m)
print(ls1)





