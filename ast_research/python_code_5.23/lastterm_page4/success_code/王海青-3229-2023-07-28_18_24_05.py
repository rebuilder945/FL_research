a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
    else:
        pass

if len(b)==0:
    print("False")
elif len(b)!=0:
    b1= ','.join(str(i) for i in b)
    print(b1)
