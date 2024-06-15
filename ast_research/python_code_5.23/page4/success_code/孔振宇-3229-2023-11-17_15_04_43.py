a=eval(input())
b=[]
for x in a:
    if a.count(x)>1:
        a.remove(x)
    if len(a)>0:
        a.sort()
        b=','.join(str(i) for i in a)
        print(b)
    else:
        print(False)
        
