a=input()
b=[]
for i in a:
    b.append(i)
d=list(map(int,b))
for i in range(len(d)):
    d[i]=(d[i]+5)%10
d.reverse()
c=[]
for i in range(len(d)):
    n=d[i]*10**(len(d)-i-1)
    c.append(n)
print(sum(c))


                

