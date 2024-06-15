aa=''.join(eval(input()))
list1=[]
list2=[]
for x in aa:
    list2.append(x)
    if x not in list1:
        list1.append(x)
list1.sort()
for x in list1:
    b=list2.count(x)
    print('{}.{}'.format(x,b))

