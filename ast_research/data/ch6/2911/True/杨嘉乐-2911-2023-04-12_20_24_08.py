n=eval(input())
l=[]
sum=0
while n:
    l.append(n%10)
    n=n//10
ll=l[:]
kk=len(ll)
for m in range(kk):
    l[m]=(l[m]+5)%10
print(str(l).replace("[","").replace("]","").replace(",","").replace(" ",""))
