n=eval(input())
sums=range(1,n+1)
sum2=[]
m=sums[0]
for i in range(len(sums)-1):
    sums.append(sums[i+1])
sum2.append(m)
print(sum2)    
