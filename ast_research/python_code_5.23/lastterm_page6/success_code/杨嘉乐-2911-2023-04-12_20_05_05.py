n=eval(input())
l=[]
i=0
sum=0
while n!=0:
    l.append(n%10)
    i+=1
    n//10
for m in range(len(l)):
    l[m]=(l[m]+5)%10
l.reverse()
for m in range(len(l)):
    sum+=l[m]*10**m
print(sum)
