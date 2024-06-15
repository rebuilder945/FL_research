a=eval(input())
ls=[]
while a>0:
    b=(a%10+5)%10
    ls.append(b)
    a=a//10
k=0
for x in range(1,len(ls)+1):
    k=k+ls[-x]*(10**(x-1))
print(k)
