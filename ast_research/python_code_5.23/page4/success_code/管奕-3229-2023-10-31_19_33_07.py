list=eval(input())
a=[]
for x in list:
    if list.count(x)==1:
        a.append(x)
        print(a.sort())
if len(list)==0:
    print('False')

    
