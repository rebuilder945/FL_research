a=input()

c='1234567890'
for i in a:
    if i not in list(c):
        a=a.replace(i,'*')
a=a.split("*")

d=[]
e=[]
for j in a:
    if j!='':
        d.append(j)

if d==[]:
    print("No digits")
else:
    max=0
    for k in d:
        if len(k)>=max:
            max=len(k)
    for j in d:
        if len(j)==max:
            e.append(j)
    print(e[-1])
            
        


