l=eval(input())
l.sort()
l1=[]
for i in l:
    if l.count(i)==1:
        l1.append(i)      
    else:
        pass
if len(l1)==0:
    print('False')
else:
    print(','.join(str(x)for x in l1))
        
