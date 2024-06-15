a=eval(input())
a=list(a)
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
        b.sort()
if b==[]:
    print("False")
else:            
    c=','.join(map(str,b))
    print(c)       
