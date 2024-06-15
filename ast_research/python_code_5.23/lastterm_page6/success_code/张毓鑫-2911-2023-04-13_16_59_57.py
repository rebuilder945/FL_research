a=input()
b=[]
for i in a:
    i=str((int(i)+5)%10)
    b.append(i)
b.reverse()
c=''
for i in b:
    c+=i
d=int(c)
e=d.zfill(len(a))
print(int(c))

