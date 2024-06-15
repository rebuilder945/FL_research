a=input()
b=[]
t=''
c=len(a)
d=0
e=0
for i in range(c):
    if a[i].isdigit():
        t+=str(a[i])
        if i!=c-1 and not a[i+1].isdigit():
            b.append(t)
            t=''
f=len(b)
if b==[]:
    print('No digits')
else:
    for i in range(f-1,-1,-1):
        if len(b[i])>d:
            d=len(b[i])
            e=b[i]
    print(e)        
    


