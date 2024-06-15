a=eval(input())
list=[]
for x in a:
    if a.count(x)==1:
        list.append(x)
        list1=list.sort(reverse=True)
        print(str(list1))
else:
    print('False')

