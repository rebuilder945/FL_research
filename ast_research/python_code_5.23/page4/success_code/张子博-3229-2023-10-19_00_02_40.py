p=eval(input())
k=[]
for i in p:
    if p.count(i)==1:
        k.append(i)
k.sort()
for m in k:
    print(m,end=',')
if  len(k)==0:
    print('False')

    

