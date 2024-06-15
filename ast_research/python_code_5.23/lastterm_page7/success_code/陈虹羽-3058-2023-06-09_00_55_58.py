a=input()
b={}
c=0
d=''
while a!='q':
    b[a]=b.get(a,0)+1
    a=input()
for i in b:
    if int(b[i])>c:
        c=int(b[i])
        d=i
print(d,c)

