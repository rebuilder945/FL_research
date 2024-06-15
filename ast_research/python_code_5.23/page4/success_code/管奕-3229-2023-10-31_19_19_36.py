list=eval(input())
a=[]
for x in list:
    if list.count(x)==1:
        a.append(x)
        print(a.sort())
    else:
        print('False')
