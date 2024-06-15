a,b,c,d=input().split()
b=int(b)
c=int(c)
d=int(d)
ff=[b,c,d]
ff.sort(reverse=True)
e=(b+c+d)/3
e=format(e,".2f")
f=[]
for i in ff:
    f.append(format(i,".2f"))
g={}
g[0]=a
g[1]=f[0]
g[2]=f[1]
g[3]=f[2]
g[4]=e
output = ""
for key, value in g.items():
    output += str(value) + " "
print(output)
