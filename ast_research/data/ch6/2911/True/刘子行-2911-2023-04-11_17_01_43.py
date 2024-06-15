a=str(input())
b=[x for x in a]
c=[]
for x in b:
    x=(int(x)+5)%10
    c.append(x)
d=''
for x in c[::-1]:
    d+=str(x)
print(d)
