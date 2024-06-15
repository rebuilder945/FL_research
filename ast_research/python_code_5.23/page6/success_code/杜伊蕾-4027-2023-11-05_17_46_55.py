b=0
d=[]
a=[]
while True:
    line = input("")
    if line == '#': 
        break
    else:
        a.append(line) 
for x in a:
    if x=="#":
        break
    else:
        c=int(x)
        b+=c
        d.append(str(c))
        n=len(d)      
print(n,b)
