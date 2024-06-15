a = eval(input())
b = []
for i in a:
    if a.count(i)==1:
        b.append(i)
b = sorted(b)
if len(b)==0:
    print("False")
else:
    for i in b:
        if b.index(i)!=len(b)-1:
            print(i,end=",")
        else:
            print(i)
