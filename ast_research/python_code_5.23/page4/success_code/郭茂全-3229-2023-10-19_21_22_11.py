list=eval(input())
a=[]
for x in list:
    if list.count(x)==1:
        a.append(x)
if a==[]:
    print(False)
else:
    a.sort()
    b=','.join(map(str,a))
    print(b)    
