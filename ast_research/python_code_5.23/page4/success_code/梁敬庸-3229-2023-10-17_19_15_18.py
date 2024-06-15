a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
b.sort()
if len(b)>0:
    for i in range(len(b)-1):
        print(b[i],end=',')
    print(b[-1])    
else:print("False")
