a=eval(input())
b=a.copy()
d=[]
for i in range (0,len(a)):
    if a.count(a[i])==1:
        d.append(a[i])
d.sort()
if d!=[]:
    for j in range(0,len(d)-1):
        print(d[j],end=',')
    print(d[-1])
else:
    print('False')
