a,b,c,d=input().split()
b=int(b)
c=int(c)
d=int(d)
e=(b+c+d)/3
b=format(b,".2f")
c=format(c,".2f")
d=format(d,".2f")
e=format(e,".2f")
f=[b,c,d]
f.sort(reverse=True)
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
