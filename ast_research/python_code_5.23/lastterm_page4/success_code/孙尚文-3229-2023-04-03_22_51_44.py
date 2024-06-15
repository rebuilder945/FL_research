a=eval(input())
b=[]
for x in a:
    if a.count(x)>1:
        b.append(a)
    else:
        print("False")
a.sort()
