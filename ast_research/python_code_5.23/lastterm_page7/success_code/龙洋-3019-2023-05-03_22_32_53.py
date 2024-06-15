x=input().split(' ')
lis=[]
for n in x[1:]:
    lis.append(float(n))
lis.sort(reverse=True)
yifa=(sum(lis))/3
name=x[0]
print(name,"%.2f %.2f %.2f %.2f"%(lis[0],lis[1],lis[2],yifa))

