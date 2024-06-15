n=eval(input())
sum=0
de=[1,2]
nu=[2,3]
if n==1:
    sum=2
elif n==2:
    sum=2+3/2
else:
    for i in range(2,n):
        de.append(de[i-2]+de[i-1])
        nu.append(nu[i-2]+nu[i-1])
    for g in range(0,len(de)):
            sum=sum+nu[g]/de[g]
print("%.4f"%sum)
