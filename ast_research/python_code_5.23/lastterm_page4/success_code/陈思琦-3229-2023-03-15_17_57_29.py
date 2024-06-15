a=eval(input())
b=[]
for i in a:
    if  a.count(i) < 2:
        b.append(i)
b.sort()
if len(b)==0:
    print("False")
else:
    b=",".join(map(str,b))
    print(b)

