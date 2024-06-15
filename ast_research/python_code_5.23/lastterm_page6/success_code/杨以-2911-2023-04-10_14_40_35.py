m=input()
s=list(m)
#print(type(m))
#print(list(m))
m1=[]
for x in list(m):
    x=(int(x)+5)%10
    m1.append(x)
for x in range(0,int(len(m1)/2)-1):
    m1[x],m1[-x-1]=m1[-x-1],m1[x]
ou=""
for i in m1:
    ou=ou+str(i)
print(ou)




