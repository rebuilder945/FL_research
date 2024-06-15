dex=str(input())
k=[]
m=''
for i in dex:
    i=int(i)+5
    d=i%10
    k.append(d)
k.reverse()
for x in k:
    m=m+str(x)
print(m)
