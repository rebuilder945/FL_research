a=eval(input())
list1=[]
for x in a:
    b=a.count(x)
    if b==1:
        list1.append(x)
if len(list1)>0:
    list1.sort()
    print(','.join(str(i)for i in list1))
else:
    print('False')
