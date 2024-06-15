m=input()
s=list(m)
m1=[]
for x in list(m):
    p=(int(x)+5)%10
    m1.append(p)
for i in range(0,int(len(m1)/2)):
    m1[i],m1[-i-1]=m1[-i-1],m1[i]
ou=""
for i in m1:
    ou=ou+str(i)
print(ou)

