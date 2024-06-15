a=input()
l=[]
for i in a:
    s=a.count(i)
    if s==1:
        l.append(i)
if len(l)>0:
    print(l[0])
else:
    print('None')
    
