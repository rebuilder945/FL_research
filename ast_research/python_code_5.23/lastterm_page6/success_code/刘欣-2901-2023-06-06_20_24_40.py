lis=[]
sum1=0
n=0
s=input() or "#"
while s!="#":
    lis.append(s)
    n+=1
    s=input() or "#"
for i in lis:
    i=int(i)
    sum1+=i
print(n,sum1)
