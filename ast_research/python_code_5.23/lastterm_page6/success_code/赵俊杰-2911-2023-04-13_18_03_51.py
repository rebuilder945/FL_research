a=eval(input())
ls=[]
while a>0:
    b=a%10
    b=(b+5)%10
    ls.append(b)
    a=a//10
c=""
for x in ls:
    c=c+str(x)
c=int(c)
print(c)
