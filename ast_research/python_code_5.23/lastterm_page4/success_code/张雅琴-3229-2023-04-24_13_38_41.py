a=eval(input())
b={}
for i in a:
    if a.count(i)==1:
        b.append(i)
        c=list(b)
        c.sort()
else:
    print("False")
