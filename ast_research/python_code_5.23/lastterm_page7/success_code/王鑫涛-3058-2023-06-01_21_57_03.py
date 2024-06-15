a = input()
b=[]
c={}
d=1
while (a!='p'):
    b.append(a)
    a= input() or 'None'
for i in b:
    c[b.count(i)]=i
    if b.count(i)>d:
        d=b.count(i)
print('%s %d'%(c[d],d))
