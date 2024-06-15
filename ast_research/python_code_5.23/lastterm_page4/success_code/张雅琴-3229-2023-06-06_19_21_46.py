a=eval(input())
b=[]
c=0
for x in a:
    if a.count(x)==1:
        b.append(x)
        c+=1
if c==0:
    print("False")
else:
    print(str(b))
