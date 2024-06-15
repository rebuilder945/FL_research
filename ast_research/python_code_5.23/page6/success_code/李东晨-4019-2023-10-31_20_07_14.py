n=str(input())
x=list(n)
z=[]
for i in x:
    v=(int(i)+5)%10
    z.append(v)
if len(z)>2:
    z[0],z[-1]=z[-1],z[0]
    z[1],z[-2]=z[-2],z[1]
    k=int(''.join(map(str,z)))
    print(k)
elif len(z)==2:
    z[0],z[-1]=z[-1],z[0]
    e=int(''.join(map(str,z)))
    print(e)
