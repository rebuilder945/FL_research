lst=eval(input())
a=set(lst)
b=[]
for x in a:
    if lst.count(x)==1:
        b.append(x)
        print("".join(b))
    else:
        print("False")
