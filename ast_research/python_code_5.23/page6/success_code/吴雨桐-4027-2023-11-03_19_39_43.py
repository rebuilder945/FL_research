n=0
le=0
ls=[]
while n !='#':
    le+=1
    n=input() 
    ls.append(n)
tot=0
for x in ls:
    if x!='#':
        tot+=int(x)
print(le-1,tot)
