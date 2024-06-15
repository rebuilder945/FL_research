n=eval(input())
l=[]
sum=0
while n!=0:
    l.append(n%10)
    n//10
for m in range(len(l)):
    l[m]=(l[m]+5)%10
l.reverse()
for p in range(len(l)):
    sum+=l[p]*10**p
print(sum)
