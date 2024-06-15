n=eval(input())
l=[]
sum=0
while n!=0:
    l.append(n%10)
    n//10
    kk=len(l)
for m in range(kk)):
    l[m]=(l[m]+5)%10
l.reverse()
for p in range(kk):
    sum+=l[p]*10**p
print(sum)
