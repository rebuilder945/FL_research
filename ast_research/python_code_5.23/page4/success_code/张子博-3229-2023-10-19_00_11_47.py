p=eval(input())
k=[]
for i in p:
    if p.count(i)==1:
        k.append(i)
k.sort()
if len(k)==1:
    print(k[0])
else:
    for m in k[0:len(k)-1]:
        print(m,end=',',sep=',')
    print(k[len(k)])
if  len(k)==0:
    print('False')

    

