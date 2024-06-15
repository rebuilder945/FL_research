a=eval(input())
b=[]
for i in a:
    if  b.count(i)<1:
        b.append(i)
b.sort()
if len(b)==0:
    print("False")
else:
    print(b)

