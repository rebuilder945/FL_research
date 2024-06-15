a=eval(input())
lst1=[]
for i in a:
    if a.count(i)==1:
        lst1.append(i)
        lst1.sort()
        b=lst1
if b==[]:
    print('False')
else:
    print(','.join(list(map(str,b))))
