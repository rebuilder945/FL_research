a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if len(b)!=0:
    b.sort()
    print(b[0:].split(','))
else:
    print("False")
