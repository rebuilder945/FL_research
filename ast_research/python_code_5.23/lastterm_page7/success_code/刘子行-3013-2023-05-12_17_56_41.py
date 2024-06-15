a=input()
dic1={}
while a!='ok':
    guo,gdp=a.split()
    dic1[guo]=gdp
    a=input()
name=list(dic1.keys())
h1=list(dic1.values())
sum1=sum(h1)
if 'Lndia' in name:
    k="yes"
else:
    k="no"
hole=[name,h1,[k],[sum1]]
for x in hole:
    print(x)
